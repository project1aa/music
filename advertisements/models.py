from django.db import models

class Advertisement(models.Model):
    url = models.URLField()
    text = models.TextField()
    image = models.ImageField(upload_to='imags/advertisements')

    def __str__(self):
        return self.url
