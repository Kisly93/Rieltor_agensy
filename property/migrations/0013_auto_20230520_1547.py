# Generated by Django 2.2.24 on 2023-05-20 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20230519_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner_name',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
