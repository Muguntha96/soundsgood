# Generated by Django 4.2.7 on 2023-11-08 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_playlist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]