# Generated by Django 2.2.7 on 2020-04-27 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0049_remove_postjob_type_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
