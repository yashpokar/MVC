from werkzeug.routing import Map, Rule


class Router:
    _registry = {}
    _controllers = {}

    @staticmethod
    def get(pattern, callback):
        Router._register('GET', pattern, callback)

    @staticmethod
    def post(pattern, callback):
        Router._register('POST', pattern, callback)

    @staticmethod
    def _register(method, pattern, callback):
        if pattern in Router._registry:
            Router._registry[pattern]['methods'].append(method)
        else:
            Router._registry[pattern] = {
                'endpoint': callback,
                'methods': [method],
            }

    @staticmethod
    def getRules():
        return Map([Rule(pattern, **rule) for pattern, rule in Router._registry.items()])
