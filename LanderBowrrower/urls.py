from django.conf.urls import include, url
from .views import index,home,single,SubmitRequest,profile,login,register,borrower_register

urlpatterns = [
    url(r'borrower_register/', borrower_register, name='borrower_register'),
    url(r'register/', register, name='register'),
    url(r'login/', login, name='login'),
    url(r'home/', home, name='home'),
    url(r'profile/', profile, name='profile'),
    url(r'single/', single, name='single'),
    url(r'request/', SubmitRequest, name='submitrequest'),
    url(r'^$', index, name='index'),


]