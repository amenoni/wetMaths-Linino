from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from models import Game

class GameResource(ModelResource):
    class Meta:
        queryset = Game.objects.all()
        resource_name = "game"
        authorization = Authorization()