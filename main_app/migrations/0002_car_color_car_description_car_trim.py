# Generated by Django 4.1.7 on 2023-04-13 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(default='primer', max_length=50),
        ),
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='car',
            name='trim',
            field=models.CharField(default='', max_length=50),
        ),
    ]