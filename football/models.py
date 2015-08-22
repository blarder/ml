import datetime

from django.db import models

from .consumers import APIConsumer


class FootballTeam(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def all_matches_for_season(self, season_start_year):
        return self.home_matches.filter(season_start_year=season_start_year) \
            | self.away_matches.filter(season_start_year=season_start_year)

    def recent_matches(self, number=40):
        all_games = self.home_matches.all() | self.away_matches.all()
        return all_games.order_by('-match_date').select_related('home_team', 'away_team')[:number]


class MatchResultManager(models.Manager):

    def match_from_datum(self, datum):
        #TODO: move this method to a form
        datum['home_team'] = FootballTeam.objects.get_or_create(name=datum['home_team'])[0]
        datum['away_team'] = FootballTeam.objects.get_or_create(name=datum['away_team'])[0]
        try:
            # Handle the two possible date formats
            datum['match_date'] = datetime.datetime.strptime(datum['match_date'], '%d/%m/%y').date()
        except ValueError:
            datum['match_date'] = datetime.datetime.strptime(datum['match_date'], '%d/%m/%Y').date()
        return MatchResult(**datum)

    def bulk_create_from_api(self, api_name, start_year):
        consumer = APIConsumer.create(self, api_name + 'Consumer', start_year)
        self.bulk_create([self.match_from_datum(datum) for datum in consumer.get_data()])


class MatchResult(models.Model):
    home_team = models.ForeignKey(FootballTeam, related_name='home_matches')
    away_team = models.ForeignKey(FootballTeam, related_name='away_matches')

    match_date = models.DateField()
    season_start_year = models.PositiveIntegerField()

    home_goals = models.PositiveSmallIntegerField()
    away_goals = models.PositiveSmallIntegerField()

    objects = MatchResultManager()

    def __str__(self):
        return self.home_team.name + ' v ' + self.away_team.name
