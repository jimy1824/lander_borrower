from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'index.html' )

# Create your views here.
def home(request):
    return render(request, 'home.html' )

# Create your views here.
def single(request):
    return render(request, 'single.html' )

def SubmitRequest(request):
    return render(request, 'submit_request.html' )

def profile(request):
    return render(request, 'profile.html' )


def login(request):
    return render(request, 'login.html' )


def register(request):
    return render(request, 'register.html' )


