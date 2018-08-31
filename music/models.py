from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.urls import reverse
import os
from datetime import timedelta
from mutagen.mp3 import MP3
from taggit.managers import TaggableManager


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


def song_directory_path(instance, filename):
    return 'files/{0}/{1}'.format(instance.singer.name, filename)

class Song(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, allow_unicode=True)
    singer = models.ForeignKey('Singer', on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    created = models.DateField(auto_now_add=True)
    duration = models.CharField(max_length=5)
    file1 = models.FileField(upload_to=song_directory_path, blank=True,
        verbose_name='File 320')
    file2 = models.FileField(upload_to=song_directory_path, blank=True,
        verbose_name='File 128')
    tags = TaggableManager()
    image = models.ImageField(upload_to=song_directory_path)
    views = models.PositiveIntegerField(default=0)
    lyrics = models.TextField(blank=True, default='')
    # order = models.AutoField()
    languages = models.ManyToManyField('Language')

    def list_genres(self):
        return ', '.join([genre.name for genre in self.genres.all()])

    def list_lagenres(self):
        return ', '.join([lang.name for lang in self.languages.all()])

    def save(self, *args, **kwargs):
        self.slug = 'دانلود-آهنگ-{}-{}'.format(self.singer.name, slugify(self.name, allow_unicode=True))
        super().save(*args, **kwargs)
        if self.file1:
            file = self.file1
        elif self.file2:
            file = self.file2
        self.duration = get_filesize(file)
        super().save(*args, **kwargs)

    def clean(self):
        if not any([self.file1, self.file2]):
            raise ValidationError('Either File 320 or File 128 must be set')


    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)
        unique_together = ('name', 'singer')

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})


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


class Language(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
