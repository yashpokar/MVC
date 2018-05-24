from .view import view


class Controller(object):
    def render_template(self, template_name, **context):
        return view(template_name, **context)
