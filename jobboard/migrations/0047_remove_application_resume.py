# Generated by Django 2.2.7 on 2020-04-27 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0046_application_jobpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='resume',
        ),
    ]
