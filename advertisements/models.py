from django.db import models

class Advertisement(models.Model):
    positions = (
        ('a', 'A'),
        ('b1', 'B1'),
        ('b2', 'B2'),
        ('c', 'C'),
        ('d1', 'D1'),
        ('d2', 'D2'),
        ('e', 'E'),
    )

    url = models.URLField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/advertisements')
    position = models.CharField(max_length=2, choices=positions)

    def __str__(self):
        return '{}, {}'.format(self.url, self.position)
