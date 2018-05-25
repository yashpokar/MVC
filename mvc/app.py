import inspect
import os
import sys
from glob import iglob
from .view import View
from .router import Router
from mvc.controller import Controller
from importlib import import_module
from jinja2 import Environment, FileSystemLoader
from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import HTTPException
from werkzeug.serving import run_simple


class App(object):
    _router = None
    _root_path = ''
    _config = ''
    _controllers = {}

    def __init__(self, root_path, config={}):
        self._root_path = root_path
        self._bootstrap()

    def _bootstrap(self):
        self._router = Router.getRules()
        self._load_template_engine()
        self._load_controllers()

    def _load_controllers(self):
        sys.path.append(os.path.join(self._root_path, 'controllers/'))

        for module in [pyfile[:-3].replace('/', '.') for pyfile in iglob(os.path.join(self._root_path, 'controllers/**/*.py'), recursive=True)]:
            module = import_module(module)

            for attr in dir(module):
                # Import controller class from modules
                attr = getattr(module, attr)

                if inspect.isclass(attr) and issubclass(attr, Controller) and attr.__module__ == module.__name__:
                    # Initialized controller
                    self._controllers[attr.__name__] = attr()
        return

    def _load_template_engine(self):
        template_path = os.path.join(self._root_path, 'templates')
        engine = Environment(loader=FileSystemLoader(template_path), autoescape=True)
        View.setEngine(engine)

    def dispatch_request(self, request: Request):
        adapter = self._router.bind_to_environ(request.environ)

        try:
            endpoint, values = adapter.match()
            response = self._class_action(*endpoint.split('@'), request, values)

            if not isinstance(response, dict):
                response = { 'response': response }

            return Response(**response)
        except HTTPException as e:
            return e

    def _class_action(self, controller, method, request, values):
        return getattr(self._controllers[controller], method)(request, **values)

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def run(self, hostname='127.0.0.1', port=5000, debug=False, reloader=False):
        return run_simple(hostname, port, self, port, debug, reloader)
