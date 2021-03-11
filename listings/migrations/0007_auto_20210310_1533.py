# Generated by Django 3.1.7 on 2021-03-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20210309_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='title',
        ),
        migrations.AddField(
            model_name='listing',
            name='land_type',
            field=models.CharField(choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Duplex', 'Duplex')], default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='sale_agreed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='sold',
            field=models.BooleanField(default=True),
        ),
    ]
