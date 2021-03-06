# Generated by Django 3.2.11 on 2022-01-25 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet_app', '0008_auto_20220125_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutritionist',
            name='bank_account',
            field=models.CharField(max_length=255, verbose_name='Konto bankowe'),
        ),
        migrations.AlterField(
            model_name='nutritionist',
            name='competence_proof',
            field=models.FileField(blank=True, null=True, upload_to='competence/', verbose_name='Potwierdzenie kompetencji'),
        ),
    ]
