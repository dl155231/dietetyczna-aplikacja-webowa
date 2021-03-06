# Generated by Django 3.2.11 on 2022-01-26 19:28

import datetime
import diet_app.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet_app', '0011_auto_20220126_1553'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consultations',
            options={'ordering': ['-date'], 'verbose_name': 'Konsultacja', 'verbose_name_plural': 'Konsultacje'},
        ),
        migrations.AddField(
            model_name='consultations',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 1, 26, 20, 28, 0, 300779), verbose_name='Godzina'),
        ),
        migrations.AlterField(
            model_name='consultations',
            name='date',
            field=models.DateField(default=datetime.date.today, validators=[diet_app.utils.present_or_future_date], verbose_name='Data'),
        ),
    ]
