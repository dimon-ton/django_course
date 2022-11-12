from django.urls import path
from .views import Home, About, Contact

urlpatterns = [
    path('', Home, name='home-page'),
    path('about', About, name='about-page'),
    path('contact', Contact, name='contact-page'),
]
