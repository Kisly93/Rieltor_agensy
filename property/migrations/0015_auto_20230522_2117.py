# Generated by Django 2.2.24 on 2023-05-22 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20230522_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner_apartment',
            new_name='apartments',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_name',
            new_name='name',
        ),
    ]
