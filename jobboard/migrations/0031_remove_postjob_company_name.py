# Generated by Django 2.2.7 on 2020-04-25 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0030_remove_postjob_logo_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postjob',
            name='company_name',
        ),
    ]
