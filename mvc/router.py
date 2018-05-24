import functools
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException


class Router:
    _registry = {
        'GET': [],
        'POST': [],
    }

    @staticmethod
    def rules():
        # TODO :: The approach over here is very bad
        return Map(functools.reduce(lambda x, y: x + y, Router._registry.values()))

    @staticmethod
    def get(pattern, callback):
        Router._register('GET', pattern, callback)

    @staticmethod
    def post(pattern, callback):
        Router._register('POST', pattern, callback)

    @staticmethod
    def _register(method, pattern, callback):
        return Router._registry[method].append(Rule(pattern, endpoint=callback))
