# Generated by Django 2.0.4 on 2018-12-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20181101_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='users/%Y/%m/%d'),
        ),
    ]
