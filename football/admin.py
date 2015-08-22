from django.contrib import admin

from .models import FootballTeam, MatchResult


@admin.register(FootballTeam)
class FootballTeamAdmin(admin.ModelAdmin):
    pass


@admin.register(MatchResult)
class MatchResultAdmin(admin.ModelAdmin):
    fields = ['home_team', 'away_team', 'home_goals', 'away_goals', 'match_date']
    list_display = ['__str__'] + fields

# Register your models here.
