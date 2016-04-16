from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core import serializers
from django.utils import timezone

from hw.hwInterface import sweepMode, shootPlayer, waitingMode
import fire


# Create your models here.
class Game(models.Model):
    WINNER_CHOICES = ((1, 'First Player'),(2, 'Second Player'),(3, 'Third Player'),)
    STATUS_CHOICES = (('n','Not Started'),('s','Started'),('f','Finished'),('c','Cancelled'),)

    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True,blank=True)
    player1 = models.TextField(null=True,blank=True)
    player2 = models.TextField(null=True,blank=True)
    player3 = models.TextField(null=True,blank=True)
    winner = models.IntegerField(null=True,blank=True,choices=WINNER_CHOICES )
    status = models.TextField(choices=STATUS_CHOICES)

    def __str__(self):
        return str(self.pk)

#Game Post Save
@receiver(post_save, sender=Game)
def launch_game(sender, instance, **kwargs):
    json = serializers.serialize('json',[instance,])

    if instance.status == 's':
        sweepMode()
    elif instance.status == 'f' or instance.status == 'c':
        waitingMode()

    fire.sendGameMessage(instance.pk,"game_update",json)


class Move(models.Model):
    PLAYER_CHOICES = ((1, 'First Player'),(2, 'Second Player'),(3, 'Third Player'),)

    game = models.ForeignKey('Game')
    player = models.IntegerField(null=True,blank=True,choices=PLAYER_CHOICES)
    time = models.DateTimeField(default= timezone.now() , blank=True)
    value = models.IntegerField()
    scoreP1 = models.IntegerField(null=True,blank=True)
    scoreP2 = models.IntegerField(null=True,blank=True)
    scoreP3 = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return "Game: %d move: %d" % (self.game.pk, self.pk)


@receiver(pre_save, sender=Move)
def process_move(sender, instance, **kwargs):
    lastMoves = Move.objects.filter(game__pk=instance.game.pk)

    if not lastMoves:
        #THIS IS THE FIRST MOVE OF THE GAME
        instance.scoreP1 = 100
        instance.scoreP2 = 100
        instance.scoreP3 = 100

        if(instance.player == 1):
            instance.scoreP1 -= instance.value
        elif(instance.player == 2):
            instance.scoreP2 -= instance.value
        else:
            instance.scoreP3 -= instance.value

    else:
        lastMove = lastMoves.latest('pk')
        if(instance.player == 1):
            instance.scoreP1 = lastMove.scoreP1 - instance.value
            instance.scoreP2 = lastMove.scoreP2
            instance.scoreP3 = lastMove.scoreP3

            if instance.scoreP1 <= 0:
                shootPlayer(1)

        elif(instance.player == 2):
            instance.scoreP1 = lastMove.scoreP1
            instance.scoreP2 = lastMove.scoreP2 - instance.value
            instance.scoreP3 = lastMove.scoreP3

            if instance.scoreP2 <= 0:
                shootPlayer(2)

        else:
            instance.scoreP1 = lastMove.scoreP1
            instance.scoreP2 = lastMove.scoreP2
            instance.scoreP3 = lastMove.scoreP3 - instance.value

            if instance.scoreP3 <= 0:
                shootPlayer(3)

    if instance.scoreP1 <= 0 and instance.scoreP2 <= 0:
        instance.game.winner = 3
        instance.game.status = 'f'
        instance.game.save()
    elif instance.scoreP2 <= 0 and instance.scoreP3 <= 0:
        instance.game.winner = 1
        instance.game.status = 'f'
        instance.game.save()
    elif instance.scoreP1 <= 0 and instance.scoreP3 <= 0:
        instance.game.winner = 2
        instance.game.status = 'f'
        instance.game.save()


@receiver(post_save, sender=Move)
def send_move(sender, instance, **kwargs):
    json = serializers.serialize('json',[instance,])
    fire.sendGameMessage(instance.game.pk,"moves",json)