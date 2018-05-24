from mvc.controller import Controller


class HomeController(Controller):
    def index(self, request):
        return 'Hello World!'
