# Generated by Django 3.0.5 on 2020-04-30 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20200429_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='user_postings/%Y/%m/%d'),
        ),
    ]