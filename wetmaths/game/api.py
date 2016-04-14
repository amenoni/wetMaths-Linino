from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
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
    game_id = fields.IntegerField()

    class Meta:
        queryset = Move.objects.all().order_by('-time')
        resource_name = "move"
        authorization = Authorization()

    def dehydrate_game_id(self, bundle):
        return bundle.obj.game.pk


    def hydrate(self, bundle):
        bundle.data['player']= int(bundle.data['player'])
        bundle.data['value'] = int(bundle.data['value'])
        return bundle

    def obj_create(self, bundle, **kwargs):
        return super(ModelResource,self).obj_create(bundle,game= Game.objects.get(pk=bundle.data.pop(
                'game_id')))