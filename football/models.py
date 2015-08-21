from django.db import models

from .consumers import FootballDataConsumer


class FootballTeam(models.Model):
    name = models.CharField(max_length=255)


class MatchResult(models.Model):
    home_team = models.ForeignKey(FootballTeam, related_name='home_matches')
    away_team = models.ForeignKey(FootballTeam, related_name='away_matches')

    match_date = models.DateField()
    season_start_year = models.PositiveIntegerField()

    home_goals = models.PositiveSmallIntegerField()
    away_goals = models.PositiveSmallIntegerField()


class MatchResultManager(models.Manager):
    def bulk_create_from_api(self, start_year):
        matches_this_season = self.filter(season_start_year=start_year).count()

        consumer = FootballDataConsumer(largest_seen_id=matches_this_season - 1)
        self.bulk_create([MatchResult(**datum) for datum in consumer.get_data_for_season(start_year)])
