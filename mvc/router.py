from .interfaces import RouterInterface, implementer
from werkzeug.routing import Map


@implementer(RouterInterface)
class Router:
    _registry = []

    @staticmethod
    def register(rules):
        Router._registry = rules

    @staticmethod
    def rules():
        return Map(Router._registry)
