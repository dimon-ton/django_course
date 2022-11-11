from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
# def Home(req):
#     return HttpResponse('<h1>Hello World</h1> <br> <p>นี่คือเว็บไซต์อันแรกของฉัน</p>')

def Home(req):
    allproduct = Product.objects.all()
    context = {'allproduct':allproduct}
    return render(req, 'company/home.html', context)

def About(req):
    return render(req, 'company/about.html')