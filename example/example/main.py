from werkzeug.wrappers import Response
from werkzeug.serving import run_simple
from mvc.app import create_app
from mvc.router import Router
from werkzeug.routing import Rule

def home(request):
    return Response('Hello World!')

def user_profile(request, username):
    return Response('Welcome %s' % username)

Router.register([
    Rule('/', endpoint=home),
    Rule('/profile/<username>', endpoint=user_profile),
])

app = create_app(Router)

if __name__ == '__main__':
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)
