# Generated by Django 3.2.11 on 2022-01-25 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diet_app', '0008_auto_20220125_2012'),
        ('accounts', '0004_alter_customuser_user_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='client',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='diet_app.client', verbose_name='Klient'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='nutritionist',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='diet_app.nutritionist', verbose_name='Dietetyk'),
        ),
    ]