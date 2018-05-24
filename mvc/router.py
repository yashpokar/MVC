from werkzeug.routing import Map, Rule


class Router:
    _registry = {
        'GET': [],
        'POST': [],
    }

    @staticmethod
    def register(rules):
        Router._registry = rules

    @staticmethod
    def rules(method):
        return Map(Router._registry[method])

    @staticmethod
    def get(pattern, callback):
        Router._registry['GET'].append(Rule(pattern, endpoint=callback))

    @staticmethod
    def post(pattern, callback):
        Router._registry['POST'].append(Rule(pattern, endpoint=callback))
