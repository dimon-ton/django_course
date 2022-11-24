from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home-page'),
    path('about', About, name='about-page'),
    path('contact', Contact, name='contact-page'),
    path('accountant', Accountant, name='accountant-page'),
    path('register', Register, name='register-page'),
    path('profile', ProfilePage, name='profile-page'),
    path('reset-password', RessetPassword, name='reset-password'),
    path('reset-new-password/<str:token>/', ResetNewPassword, name='reset-new-password'),
    path('verify-email/<str:token>/', Verify_Success, name='verify-email'),
    path('action-detail/<str:cId>/', ActionPage, name='action-page'),
    path('add-product', Addproduct, name='addproduct-page'),
    # AJAX Example
    path('crud/',  CrudView.as_view(), name='crud_ajax'),
    path('ajax/crud/create/',  CreateCrudUser.as_view(), name='crud_ajax_create'),
]
