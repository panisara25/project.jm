# Generated by Django 2.2.7 on 2020-04-25 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_application_jobpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='jobpost',
        ),
    ]
