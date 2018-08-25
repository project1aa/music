from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return '{} - {}'.format(self.name, self.email)
