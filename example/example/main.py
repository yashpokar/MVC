import os
from mvc.app import App
from mvc.router import Router
from routes import home, user_profile

Router.get('/', home)
Router.get('/profile/<username>', user_profile)

app = App(os.path.dirname(__file__))

if __name__ == '__main__':
    app.run(debug=True)
