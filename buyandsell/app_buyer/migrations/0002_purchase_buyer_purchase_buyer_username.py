# Generated by Django 4.2.1 on 2023-06-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_buyer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='buyer',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='purchase',
            name='buyer_username',
            field=models.CharField(default=None, max_length=200),
        ),
    ]