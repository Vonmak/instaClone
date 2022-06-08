# Generated by Django 4.0.5 on 2022-06-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0016_remove_profile_email_profile_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
