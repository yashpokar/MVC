from mvc.controller import Controller


class ProfileController(Controller):
    def show(self, request, username):
        return 'Hello ' + username
