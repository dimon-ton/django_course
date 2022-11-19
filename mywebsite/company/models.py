from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype = models.CharField(max_length=100, default='member')
    point = models.IntegerField(default=0)
    tel = models.CharField(max_length=20, null=True, blank=True)
    verified = models.BooleanField(default=False)
    verified_token = models.CharField(max_length=100, default='no token')

    def __str__(self):
        return self.user.username

'''
    Product
    - procuct (Char)
    - description (Text)
    - price (Int)
    - quantity (Int)

'''

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(default=1,null=True, blank=True)
    instock = models.BooleanField(default=True)
    # file
    picture = models.ImageField(upload_to='product', null=True, blank=True)
    relatedFile = models.FileField(upload_to='product', null=True, blank=True)

    def __str__(self):
        return self.title


'''
รัน 2 คำสั่งนี้ที่มีการสร้่าง model ใหม่หรือมีการเปลี่ยนแปลง
python manage.py makemigration
python manage.py migrate
'''
class ContactList(models.Model):
    title = models.CharField(max_length=400)
    email = models.CharField(max_length=200)
    detail = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title + " " + self.email


class ResetPasswordToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Action(models.Model):
    contactlist = models.ForeignKey(ContactList, on_delete=models.CASCADE)
    action_detail = models.TextField()


    def __str__(self):
        return '%s - %s' % (self.contactlist, self.action_detail)