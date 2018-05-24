from mvc.controller import Controller


class HomeController(Controller):
    def index(self, request):
        return self.render_template('home.html')
