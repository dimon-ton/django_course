from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from songline import Sendline
from .emailSystem import sendthai
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import uuid


# Create your views here.
# def Home(req):
#     return HttpResponse('<h1>Hello World</h1> <br> <p>นี่คือเว็บไซต์อันแรกของฉัน</p>')

def Home(req):
	allproduct = Product.objects.all()
	context = {'allproduct':allproduct}
	return render(req, 'company/home.html', context)

def About(req):
	return render(req, 'company/about.html')

@login_required
def Accountant(req):

	# if req.user.profile.usertype != 'accountant':
	allow_user = ['accountant','admin']
	if req.user.profile.usertype not in allow_user:
		return redirect('home-page')

	allcontact = ContactList.objects.all().order_by('-id')
	# allcontact = ContactList.objects.all()
	context = {'allcontact':allcontact}
	return render(req, 'company/accountant.html', context)

  
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
			return redirect('profile-page')
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

		# send mail
		text = 'สวัสดีคุณลูกค้า\nอีเมลของคุณคือ {} \nเราได้รับปัญหาที่ท่านสอบถามเรียบร้อยแล้วจะรีบตอบกลับโดยเร็วที่สุด'.format(email)

		sendthai(email, 'Pimon Company: สอบถามปัญหา', text)

		# send line
		token = '4ED99HkYOoqVUEdd6SPN4OOegI3S7zqu5ZYYwi5QstA'
		m = Sendline(token)
		m.sendtext('หัวข้อ:{} \nอีเมล: {} \nรายละเอียด:{}'.format(title, email, detail))

	return render(req, 'company/contact.html', context)


# from django.contrib.auth.models import User
def Register(req):

	context = {}

	if req.method == 'POST':
		data = req.POST.copy()
		fullname = data.get('fullname')
		tel_number = data.get('tel')
		username = data.get('username')
		password = data.get('password')
		password2 = data.get('password2')

		print(data)

	   
		try:
			check = User.objects.get(username=username)
			context['warning'] = 'email {} ถูกสมัครไปแล้ว กรุณาใช้ email อื่น'.format(username)
			context['fullname'] = fullname
			return render(req, 'company/register.html', context)
		except:

			if password != password2:
				context['warning'] = 'กรุณากรอกรหัสผ่านให้ถูกต้องทั้งสองช่อง'
				return render(req, 'company/register.html', context)

			newuser = User()
			newuser.username = username
			newuser.email = username
			newuser.first_name = fullname
			newuser.set_password(password)
			newuser.save()

			u = uuid.uuid1()
			token = str(u)

			newprofile = Profile()
			newprofile.user = User.objects.get(username=username)
			newprofile.tel = tel_number
			newprofile.verified_token = token
			newprofile.save()
			sendthai(username, 'plese verify email','กรุณากดลิงค์เพื่อยืนยันการเป็นสมาชิก : \nhttp://localhost:8000/verify-email/{}'.format(token))


		try:
			user = authenticate(username=username, password=password)
			login(req, user)
		except:
			context['message'] = 'username หรือ password ไม่ถูกต้อง'

		return redirect('profile-page')

	return render(req, 'company/register.html', context)


def Verify_Success(req, token):

	context = {}

	try:
		check = Profile.objects.get(verified_token=token)
		check.verified = True
		check.point = 100
		check.save()


	except Exception as e:
		print('error: ', e)
		context['error'] = 'ลิงค์สำหรับยืนยันสมาชิกของคุณไม่ถูกต้อง กรุณาก็อบปี้ลิงค์มาวางบนเว็บบราวเซอร์แทน'


	return render(req, 'company/verify_email.html', context)


@login_required
def ProfilePage(req):
	context = {}
	profileuser = Profile.objects.get(user=req.user)
	context['profile'] = profileuser
	return render(req, 'company/profile.html', context)


def RessetPassword(req):

	context = {}

	if req.method == 'POST':
		data = req.POST.copy()
		username = data.get('username')

		print(data)
		print(username)


		try:
			user = User.objects.get(username=username)
			u = uuid.uuid1()
			token = str(u)
			newreset = ResetPasswordToken()
			newreset.user = user
			newreset.token = token
			newreset.save()

			print(token)

			sendthai(username, 'reset password link เรียน Django','กรุณากดลิงค์เพื่อ reset password: \nhttp://localhost:8000/reset-new-password/{}'.format(token))
			# https://uncleshop.com/reset-new-password/{รหัส token}
			
			email = username
			context['message'] = 'กรุณาตรวจสอบ email: {} เพื่อกดรีเซ็ต password'.format(email)
		except:
			context['message'] = 'email ของคุณไม่มีในระบบกรุณาตรวจสอบหรือสมัครสมาชิกใหม่'

	return render(req, 'company/reset_password.html', context)


def ResetNewPassword(req, token):
	context = {}
	print('token: ', token)
	try:
		check = ResetPasswordToken.objects.get(token=token)

		if req.method == 'POST':
			data = req.POST.copy()
			password1 = data.get('resetpassword1')
			password2 = data.get('resetpassword2')

			if password1 == password2:
				user = check.user
				user.set_password(password1)
				user.save()

				user = authenticate(username=user.username, password=password1)
				login(req, user)
				return redirect('profile-page')
			else:
				context['error'] = 'คุณกรอกรหัสไม่ตรงกัน'


	except Exception as e:
		print('error: ', e)
		context['error'] = 'ลิงค์สำหรับ reset รหัสผ่านของคุณไม่ถูกต้อง กรุณารีเซ็ตใหม่'


	return render(req, 'company/reset_new_password.html', context)

def ActionPage(req, cId):
	# cId = contactlist ID
	context = {}
	contact = ContactList.objects.get(id=cId)
	context['contact'] = contact

	
	if req.method == 'POST':
		data = req.POST.copy()
		print(data)
		if 'save' in data:
			print('save')
		elif 'delete' in data:
			print('delete')
		elif 'completed' in data:
			print('mark complete')


	return render(req, 'company/action.html', context)
