from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    owner = models.ForeignKey(User)
    url = models.CharField(max_length=40, unique = True)
    name = models.CharField(max_length=40)
    desc = models.TextField()
    tile2 = models.FileField(upload_to='tiles')
    tile4 = models.FileField(upload_to='tiles')
    tile8 = models.FileField(upload_to='tiles')
    tile16 = models.FileField(upload_to='tiles')
    tile32 = models.FileField(upload_to='tiles')
    tile64 = models.FileField(upload_to='tiles')
    tile128 = models.FileField(upload_to='tiles')
    tile256 = models.FileField(upload_to='tiles')
    tile512 = models.FileField(upload_to='tiles')
    tile1024 = models.FileField(upload_to='tiles')
    tile2048 = models.FileField(upload_to='tiles')

    def __unicode__(self):
        return self.name