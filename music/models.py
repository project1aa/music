from django.db import models

# Models:
#   Genre: name
#   Singer: name, birthday, genre, image
#   Song: name, genre, type, created, length, file, tags, image, views
# comment:
#
# name, age,

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Singer(models.Model):
    name = models.CharField(max_length=255)
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

    name = models.CharField(max_length=255)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    type = models.CharField(max_length=255, choices=types)
    created = models.DateField()
    duration = models.TimeField()
    file1 = models.FileField(upload_to='files/songs/', blank=True)
    descrtion1 = models.CharField(max_length=32, blank=True)
    file2 = models.FileField(upload_to='files/songs/', blank=True)
    descrtion2 = models.CharField(max_length=32, blank=True)
    # tags
    image = models.ImageField(upload_to='files/images/songs')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)
