# Generated by Django 2.2.7 on 2020-04-25 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0031_remove_postjob_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postjob',
            name='company_address',
        ),
        migrations.RemoveField(
            model_name='postjob',
            name='company_detail',
        ),
    ]