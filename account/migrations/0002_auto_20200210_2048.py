# Generated by Django 2.2.7 on 2020-02-10 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='userprofile.png', upload_to='profile_pics'),
        ),
    ]