# Generated by Django 4.0.6 on 2022-07-19 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telebot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telebot',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
