# Generated by Django 2.0.8 on 2018-10-18 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_studentprofile_rfid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='subject',
        ),
    ]
