from django.urls import path
from .views import Home, About

urlpatterns = [
    path('', Home, name='home-page'),
    path('about', About, name='about-page'),
]
