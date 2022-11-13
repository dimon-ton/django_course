from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from songline import Sendline
from django.contrib.auth import authenticate, login 


# Create your views here.
# def Home(req):
#     return HttpResponse('<h1>Hello World</h1> <br> <p>นี่คือเว็บไซต์อันแรกของฉัน</p>')

def Home(req):
    allproduct = Product.objects.all()
    context = {'allproduct':allproduct}
    return render(req, 'company/home.html', context)

def About(req):
    return render(req, 'company/about.html')

  
def Login(req):

    context = {}

    if req.method == 'POST':
        data = req.POST.copy()
        username = data.get('username')
        password = data.get('password')

        print(data)
        print(username)
        print(password)

        try:
            user = authenticate(username=username, password=password)
            login(req, user)
        except:
            context['message'] = 'username หรือ password ไม่ถูกต้อง'

    return render(req, 'company/login.html', context)

def Contact(req):

    context = {}

    if req.method == 'POST':
        data = req.POST.copy()
        title = data.get('title')
        email = data.get('email')
        detail = data.get('detail')
        print(data)
        print(title)
        print(email)
        print(detail)

        # กรณีที่ user ไม่กรอกข้อมูล
        if title == '' and email == '':
            context['message'] = 'กรุณากรอกอีเมลและหัวข้อ'
            return render(req, 'company/contact.html', context)

        # ทำการบันทึกข้อมูล
        # ContactList(title=title, email=email, detail=detail).save()
        newrecord = ContactList()
        newrecord.title = title
        newrecord.email = email
        newrecord.detail = detail
        newrecord.save()

        context['message'] = 'ข้อความถูกส่งเรียบร้อย'

        # send line
        token = '4ED99HkYOoqVUEdd6SPN4OOegI3S7zqu5ZYYwi5QstA'
        m = Sendline(token)
        m.sendtext('หัวข้อ:{} \nอีเมล: {} \nรายละเอียด:{}'.format(title, email, detail))

    return render(req, 'company/contact.html', context)