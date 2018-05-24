from zope.interface import Interface
from zope.interface import implementer


class RouterInterface(Interface):
    def rules():
        """Return object of werkzeug.routing.Map"""

