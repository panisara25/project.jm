# Generated by Django 2.2.7 on 2020-02-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0013_postjob_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
