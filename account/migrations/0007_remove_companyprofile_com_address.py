# Generated by Django 2.2.7 on 2020-02-21 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_companyprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyprofile',
            name='com_address',
        ),
    ]