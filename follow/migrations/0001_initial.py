# Generated by Django 3.0.6 on 2020-06-08 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.ManyToManyField(related_name='followed', to=settings.AUTH_USER_MODEL)),
                ('follower', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('followings', models.ManyToManyField(related_name='followings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
