# Generated by Django 2.2.10 on 2020-02-15 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confession', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='confession',
            old_name='hunter',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='confession',
            old_name='url',
            new_name='body',
        ),
    ]