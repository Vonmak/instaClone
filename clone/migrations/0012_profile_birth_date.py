# Generated by Django 4.0.5 on 2022-06-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0011_rename_comment_owner_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
