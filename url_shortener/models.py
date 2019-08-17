from django.db import models

class Url(models.Model):
    url = models.CharField(max_length=255)
    shortname = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.url
