# Generated by Django 3.2.11 on 2022-01-22 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet_app', '0003_auto_20220122_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='diet',
            name='name_diet',
            field=models.CharField(max_length=255, null=True, verbose_name='Nazwa diety'),
        ),
    ]
