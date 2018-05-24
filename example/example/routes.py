from mvc.view import view

def home(request):
    return view('home.html')

def user_profile(request, username):
    return view('profile.html', username=username)
