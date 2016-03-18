from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from hw.hwInterface import sweepMode


# Create your models here.
class Game(models.Model):
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True,blank=True)


#Game Post Save
@receiver(post_save, sender=Game)
def launch_game(sender, instance, **kwargs):
    print "HOLA QUE HACE!!!!! %s" % instance.started_at
    sweepMode()