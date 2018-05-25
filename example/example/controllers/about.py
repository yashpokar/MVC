from mvc.controller import Controller

# Bad naming convension
class Contact(Controller):
    def index(self, request):
        return 'Contact page'
