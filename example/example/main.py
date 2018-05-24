import os
from mvc.app import App
from routes import Router

app = App(os.path.dirname(__file__))

if __name__ == '__main__':
    app.run(debug=True)
