# Generated by Django 2.2.10 on 2020-02-15 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200215_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='year_of_birth',
        ),
        migrations.AddField(
            model_name='account',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 15, 18, 12, 58, 842310)),
        ),
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default='D:\\python\\jsclub-project\\static\\avatar.png', upload_to='images/'),
        ),
    ]
