# Generated by Django 3.2.7 on 2021-10-09 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_slider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='img3',
        ),
    ]