# Generated by Django 2.2.7 on 2020-02-18 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0016_postjob_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='postjob',
            name='benafit',
            field=models.TextField(null=True),
        ),
    ]
