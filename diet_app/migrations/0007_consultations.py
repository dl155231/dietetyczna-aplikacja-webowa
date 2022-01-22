# Generated by Django 3.2.11 on 2022-01-22 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diet_app', '0006_dietday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Data')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='diet_app.client', verbose_name='Klient')),
                ('nutritionist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='diet_app.nutritionist', verbose_name='Dietetyk')),
            ],
            options={
                'verbose_name': 'Konsultacja',
                'verbose_name_plural': 'Konsultacje',
            },
        ),
    ]