# Generated by Django 3.2 on 2022-11-19 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_auto_20221118_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='relatedFile',
            field=models.FileField(blank=True, null=True, upload_to='product'),
        ),
    ]
