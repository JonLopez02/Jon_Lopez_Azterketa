from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Pertsona(models.Model):
    izena = models.TextField(max_length=30)
    abizena = models.TextField(max_length=30)
    herria = models.TextField(max_length=30)

    def __str__(self):
        return u'%s' % self.izena