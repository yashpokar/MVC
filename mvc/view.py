from jinja2 import Environment, FileSystemLoader
from werkzeug.wrappers import Response


class View:
    _engine = None

    @staticmethod
    def setEngine(engine):
        View._engine = engine

    @staticmethod
    def getEngine():
        return View._engine

    @staticmethod
    def make(template_name, **context):
        view = View.getEngine().get_template(template_name)
        return { 'response': view.render(context), 'mimetype': 'text/html' }


def view(template_name, **context):
    return View.make(template_name, **context)
