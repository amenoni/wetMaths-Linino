from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from models import Game

class GameResource(ModelResource):
    class Meta:
        queryset = Game.objects.all()
        resource_name = "game"
        authorization = Authorization()

class CurrentGameResource(ModelResource):
    class Meta:
        queryset = Game.objects.filter(status='n').order_by('-started_at');
        resource_name = "currentgame"
        authorization = Authorization()
        limit = 1