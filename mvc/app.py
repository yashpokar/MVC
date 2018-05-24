import os
from werkzeug.wrappers import Request
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader


class Application(object):
    _router = None

    def __init__(self, router, config={}):
        self._router = router.rules()

    def dispatch_request(self, request):
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


def create_app(router, with_static=True):
    app = Application(router)

    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
    return app
