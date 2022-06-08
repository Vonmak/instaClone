# Generated by Django 4.0.5 on 2022-06-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0015_remove_profile_birth_date_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='', max_length=254),
        ),
    ]