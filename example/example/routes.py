from mvc.router import Router

Router.get('/', 'HomeController@index')
Router.get('/profile/<username>', 'ProfileController@show')
Router.get('/contact', 'Contact@index')
Router.get('/auth/signup', 'RegisterController@form')
