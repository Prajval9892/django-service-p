# Generated by Django 3.2.7 on 2021-10-09 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_auto_20211009_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='slider',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]