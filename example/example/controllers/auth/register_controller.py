from mvc.controller import Controller


class RegisterController(Controller):
    def form(self, request):
        return 'Sign up form from another directory'
