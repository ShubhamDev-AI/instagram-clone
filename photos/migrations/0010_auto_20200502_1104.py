# Generated by Django 3.0.5 on 2020-05-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0009_auto_20200430_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='user_postings'),
        ),
    ]