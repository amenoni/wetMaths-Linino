from django.contrib import admin
from models import Game, Move

# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ('pk','started_at','ended_at','status')

class MoveAdmin(admin.ModelAdmin):
    list_display = ('game_id','pk','player')
    list_filter = ('game_id',)

admin.site.register(Game,GameAdmin)
admin.site.register(Move,MoveAdmin)