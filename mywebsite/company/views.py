from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Home(req):
    return HttpResponse('<h1>Hello World</h1> <br> <p>นี่คือเว็บไซต์อันแรกของฉัน</p>')