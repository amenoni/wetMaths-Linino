from django.contrib import admin
from models import Game

# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ('pk','started_at','ended_at','status')

admin.site.register(Game,GameAdmin)