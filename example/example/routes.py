from views import user_profile
from mvc.router import Router

Router.get('/', 'home_controller.HomeController@index')
Router.get('/profile/<username>', 'profile_controller.ProfileController@show')
