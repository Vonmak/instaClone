# Generated by Django 4.0.5 on 2022-06-05 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0010_alter_comment_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_owner',
            new_name='user',
        ),
    ]
