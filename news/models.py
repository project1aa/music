from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    text = TextField()

    def __str__(self):
        return self.title
