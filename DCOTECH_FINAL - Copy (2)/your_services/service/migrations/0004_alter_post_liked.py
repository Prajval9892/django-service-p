# Generated by Django 3.2.7 on 2021-10-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_likee_user_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='liked',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
