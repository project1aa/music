from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    is_read = models.BooleanField(default=False)
