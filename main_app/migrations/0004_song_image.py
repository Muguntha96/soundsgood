# Generated by Django 4.2.7 on 2023-11-06 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_song_audio_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.ImageField(default='null', upload_to='images/'),
            preserve_default=False,
        ),
    ]