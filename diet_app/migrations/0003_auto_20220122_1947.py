# Generated by Django 3.2.11 on 2022-01-22 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet_app', '0002_diet_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diet',
            name='days',
        ),
        migrations.AddField(
            model_name='diet',
            name='day_end',
            field=models.DateField(default=datetime.date.today, verbose_name='Koniec diety'),
        ),
        migrations.AddField(
            model_name='diet',
            name='day_zero',
            field=models.DateField(default=datetime.date.today, verbose_name='Początek diety'),
        ),
    ]