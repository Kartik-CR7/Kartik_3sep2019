# Generated by Django 2.2.4 on 2019-09-18 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0004_auto_20190819_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdetails',
            name='Last_Name',
        ),
    ]
