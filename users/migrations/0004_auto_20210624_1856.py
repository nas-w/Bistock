# Generated by Django 3.0.8 on 2021-06-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210624_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='telephone',
            field=models.CharField(default='', max_length=30),
        ),
    ]
