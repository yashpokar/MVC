import os
from werkzeug.serving import run_simple
from mvc.app import Application
from mvc.router import Router
from routes import home, user_profile

Router.get('/', home)
Router.get('/profile/<username>', user_profile)

app = Application(
    os.path.dirname(__file__), Router
)

if __name__ == '__main__':
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)
