# Generated by Django 3.0.6 on 2020-06-07 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0014_remove_photo_is_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='tagged',
        ),
        migrations.CreateModel(
            name='Tagged',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tagged', to='photos.Photo')),
                ('tagged', models.ManyToManyField(related_name='tagged', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
