# Generated by Django 3.0.5 on 2020-04-29 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200428_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('email', 'Email'), ('facebook', 'Facebook')], default='email', max_length=30),
        ),
    ]