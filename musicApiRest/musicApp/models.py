from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} by {self.artist}"