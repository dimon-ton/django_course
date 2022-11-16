from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product) # ทำให้แอดมินสามารถเห็นข้อมูล database
admin.site.register(ContactList)
admin.site.register(Profile)
admin.site.register(ResetPasswordToken)