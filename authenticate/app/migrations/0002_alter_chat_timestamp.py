# Generated by Django 4.2.6 on 2023-11-07 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]