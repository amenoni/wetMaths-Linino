from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from models import Game,Move

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

class MoveResource(ModelResource):
    class Meta:
        queryset = Move.objects.all()
        resource_name = "move"
        authorization = Authorization()