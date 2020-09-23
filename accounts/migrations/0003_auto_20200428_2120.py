# Generated by Django 3.0.5 on 2020-04-28 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='posts',
            field=models.IntegerField(default=0),
        ),
    ]