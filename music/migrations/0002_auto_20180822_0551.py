# Generated by Django 2.1 on 2018-08-22 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='type',
            field=models.CharField(choices=[('mp3', 'MP3'), ('wav', 'WAV'), ('ogg', 'OGG')], default='mp3', max_length=255),
        ),
    ]