# Generated by Django 2.2.7 on 2020-02-18 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0012_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='postjob',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobboard.Location'),
        ),
    ]