import sys
from importlib import import_module
from werkzeug.routing import Map, Rule


class Router:
    _registry = {}
    _controllers = {}
    _controller_namespace = 'controllers'

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

    @staticmethod
    def getRequestHandler(root_path, handler):
        sys.path.append(root_path + '/controllers/')

        controller, method = handler.split('@')
        *controller_namespace, controller_class = controller.split('.')

        if controller not in Router._controllers:
            module = import_module('controllers.' + '.'.join(controller_namespace))
            Router._controllers[controller_class] = getattr(module, controller_class)()

        return getattr(Router._controllers[controller_class], method)
