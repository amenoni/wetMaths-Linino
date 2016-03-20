from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from hw.hwInterface import sweepMode
from fire import sendMessage


# Create your models here.
class Game(models.Model):
    WINNER_CHOICES = (
    ('1', 'First Player'),
    ('2', 'Second Player'),
    ('3', 'Third Player'),
    )

    STATUS_CHOICES = (
        ('n','Not Started'),
        ('s','Started'),
        ('f','Finished'),
        ('c','Cancelled'),
    )

    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True,blank=True)
    player1 = models.TextField(null=True,blank=True)
    player2 = models.TextField(null=True,blank=True)
    player3 = models.TextField(null=True,blank=True)
    winner = models.IntegerField(null=True,blank=True,choices=WINNER_CHOICES )
    status = models.TextField(max_length=1,choices=STATUS_CHOICES)


#Game Post Save
@receiver(post_save, sender=Game)
def launch_game(sender, instance, **kwargs):
    print "HOLA QUE HACE!!!!! %s" % instance.started_at
    #TODO uncoment
    sendMessage("jajajajajaja")
    #sweepMode()