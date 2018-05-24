import os
from werkzeug.wrappers import Response
from werkzeug.serving import run_simple
from mvc.app import create_app
from mvc.router import Router
from mvc.view import view
from werkzeug.routing import Rule

def home(request):
    return view('home.html')

def user_profile(request, username):
    return view('profile.html', username=username)

Router.register([
    Rule('/', endpoint=home),
    Rule('/profile/<username>', endpoint=user_profile),
])

app = create_app(os.path.dirname(__file__), Router)

if __name__ == '__main__':
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)
