# Generated by Django 4.0.5 on 2022-06-05 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
