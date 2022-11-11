from django.db import models

# Create your models here.

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
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


'''
รัน 2 คำสั่งนี้ที่มีการสร้่าง model ใหม่หรือมีการเปลี่ยนแปลง
python manage.py makemigration
python manage.py migrate
'''
