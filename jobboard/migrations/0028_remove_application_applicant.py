# Generated by Django 2.2.7 on 2020-02-23 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0027_application'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='applicant',
        ),
    ]
