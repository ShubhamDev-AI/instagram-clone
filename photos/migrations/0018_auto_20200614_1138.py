# Generated by Django 3.0.6 on 2020-06-14 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0017_auto_20200609_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='tagperson',
        ),
        migrations.AlterField(
            model_name='likes',
            name='photo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='photos.Photo'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='content',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]