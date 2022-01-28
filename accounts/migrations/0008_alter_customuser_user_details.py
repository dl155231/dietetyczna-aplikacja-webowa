# Generated by Django 3.2.11 on 2022-01-28 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diet_app', '0015_consultations_is_accepted'),
        ('accounts', '0007_remove_customuser_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_details',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='diet_app.userdetails', verbose_name='Szczegóły użytkownika'),
        ),
    ]
