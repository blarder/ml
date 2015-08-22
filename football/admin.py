from django.contrib import admin

from .models import FootballTeam, MatchResult


@admin.register(FootballTeam)
class FootballTeamAdmin(admin.ModelAdmin):
    pass


@admin.register(MatchResult)
class MatchResultAdmin(admin.ModelAdmin):
    pass

# Register your models here.
