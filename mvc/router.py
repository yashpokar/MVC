from werkzeug.exceptions import HTTPException
from werkzeug.routing import Map, Rule


class Router:
    _registry = {
        'GET': {},
        'POST': {},
    }

    @staticmethod
    def get(pattern, callback):
        Router._register('GET', pattern, callback)

    @staticmethod
    def post(pattern, callback):
        Router._register('POST', pattern, callback)

    @staticmethod
    def _register(method, pattern, callback):
        Router._registry[method][pattern] = callback

    @staticmethod
    def getRules():
        rules = []

        for routes in Router._registry.values():
            for pattern, callback in routes.items():
                rules.append(Rule(pattern, endpoint=callback))

        return Map(rules)

    @staticmethod
    def dispatch_request(registry, request):
        adapter = registry.bind_to_environ(request.environ)

        try:
            endpoint, values = adapter.match()
            return endpoint(request, **values)
        except HTTPException as e:
            return e
