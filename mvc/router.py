from werkzeug.routing import Map


class Router:
    _registry = []

    @staticmethod
    def register(rules):
        Router._registry = rules

    @staticmethod
    def rules():
        return Map(Router._registry)
