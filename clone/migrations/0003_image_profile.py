# Generated by Django 4.0.5 on 2022-06-05 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0002_remove_image_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clone.profile'),
        ),
    ]