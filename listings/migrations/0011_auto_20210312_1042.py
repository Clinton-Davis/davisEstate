# Generated by Django 3.1.7 on 2021-03-12 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_auto_20210312_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]