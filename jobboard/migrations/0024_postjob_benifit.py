# Generated by Django 2.2.7 on 2020-02-19 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0023_remove_postjob_benafit'),
    ]

    operations = [
        migrations.AddField(
            model_name='postjob',
            name='benifit',
            field=models.TextField(null=True),
        ),
    ]
