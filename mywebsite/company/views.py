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

def Contact(req):
    if req.method == 'POST':
        data = req.POST.copy()
        title = data.get('title')
        email = data.get('email')
        detail = data.get('detail')
        print(data)
        print(title)
        print(email)
        print(detail)
    return render(req, 'company/contact.html')