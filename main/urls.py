from django.urls import path
from main.views import *

urlpatterns = [
    path('', home, name='home'),
    path('home', home, name='home'),
    path('news', news, name='news'),
    path('about', about, name='about'),
    path('blogs', blogs, name='blogs'),
]
