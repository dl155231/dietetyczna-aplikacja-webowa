# Generated by Django 3.2.11 on 2022-01-22 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diet_app', '0007_consultations'),
        ('accounts', '0003_alter_customuser_user_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='diet_app.userdetails', verbose_name='Szczegóły użytkownika'),
        ),
    ]
