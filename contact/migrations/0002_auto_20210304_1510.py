# Generated by Django 3.1.7 on 2021-03-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='agent_email',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='contact',
            name='agent_name',
            field=models.CharField(default=0, max_length=200),
        ),
    ]