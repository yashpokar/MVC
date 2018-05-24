from views import home, user_profile
from mvc.router import Router

Router.get('/', home)
Router.post('/profile/<username>', user_profile)
