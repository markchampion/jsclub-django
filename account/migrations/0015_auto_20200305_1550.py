# Generated by Django 2.2.10 on 2020-03-05 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20200305_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default='/Users/macbook/Documents/safe/static/avatar.png', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='account',
            name='dob',
            field=models.DateField(default=datetime.datetime(2020, 3, 5, 15, 50, 52, 367275)),
        ),
    ]
