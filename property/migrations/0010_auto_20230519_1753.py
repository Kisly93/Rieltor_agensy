# Generated by Django 2.2.24 on 2023-05-19 15:53

from django.db import migrations


def get_flat_to_owner(apps, shcema_epitor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all().iterator():
        Owner.objects.get_or_create(
            owner_name=flat.name,
            phonenumber=flat.owners_phonenumber,
            pure_phone=flat.owner_pure_phone
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20230519_1750'),
    ]

    operations = [
        migrations.RunPython(get_flat_to_owner)
    ]
