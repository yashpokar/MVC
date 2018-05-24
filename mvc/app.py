import os
from .view import View
from .router import Router
from jinja2 import Environment, FileSystemLoader
from werkzeug.wrappers import Request
from werkzeug.exceptions import HTTPException
from werkzeug.serving import run_simple


class App(object):
    _router = None

    def __init__(self, root_path, config={}):
        self._router = Router.rules()
        template_path = os.path.join(root_path, 'templates')
        engine = Environment(loader=FileSystemLoader(template_path), autoescape=True)
        View.setEngine(engine)

    def dispatch_request(self, request: Request):
        adapter = self._router.bind_to_environ(request.environ)

        try:
            endpoint, values = adapter.match()
            return endpoint(request, **values)
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def run(self, hostname='127.0.0.1', port=5000, debug=False, reloader=False):
        return run_simple(hostname, port, self, port, debug, reloader)
