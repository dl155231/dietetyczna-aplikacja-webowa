# Generated by Django 3.2.11 on 2022-01-25 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diet_app', '0007_consultations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.RemoveField(
            model_name='nutritionist',
            name='user',
        ),
    ]