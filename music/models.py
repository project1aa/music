from django.db import models
from django.core.exceptions import ValidationError
import os
from datetime import timedelta
from mutagen.mp3 import MP3


# Models:
#   Song: name, genre, type, created, length, file, tags, image, views
# comment:
#
# name, age,

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Singer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    genre = models.ManyToManyField(Genre)
    image = models.ImageField(upload_to='files/images/singers/', blank=True)
    birthday = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    types = (
        ('mp3', 'MP3'),
        ('wav', 'WAV'),
        ('ogg', 'OGG'),
    )

    name = models.CharField(max_length=255, unique=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    type = models.CharField(max_length=255, choices=types, default='mp3')
    created = models.DateField()
    duration = models.CharField(max_length=5)
    file1 = models.FileField(upload_to='files/songs/', blank=True)
    file2 = models.FileField(upload_to='files/songs/', blank=True)
    # tags
    image = models.ImageField(upload_to='files/images/songs')
    views = models.PositiveIntegerField(default=0)
    layrics = models.TextField(blank=True, default='')

    def list_genres(self):
        return ', '.join([genre.name for genre in self.genres.all()])


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.duration = get_filesize(self.file1.path)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)


def get_filesize(filename):
    try:
        audio = MP3(filename)
        length = audio.info.length
        td = str(timedelta(seconds=length))
        tds = td.split(':')
        minutes = tds[1]
        seconds = tds[2].split('.')[0]
        return '{}:{}'.format(minutes, seconds)
    except FileNotFoundError:
        raise ValidationError('Found Not Found')
