# Generated by Django 4.1.4 on 2022-12-27 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(),
        ),
    ]
