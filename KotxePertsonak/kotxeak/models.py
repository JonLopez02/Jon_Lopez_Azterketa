from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Kotxe(models.Model):
    izena = models.TextField(max_length=30)
    alokatze_data = models.TextField(max_length=50)
    kolorea = models.TextField(max_length=20)
    modeloa = models.TextField(max_length=30)
    prezioa = models.IntegerField()

    def __str__(self):
        return u'%s' % self.izena