# Generated by Django 3.2.11 on 2022-01-26 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_is_nutritionist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='client',
        ),
    ]
