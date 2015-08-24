import datetime

from django.db import models, transaction

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


class Referee(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MatchResultManager(models.Manager):

    def match_from_datum(self, datum, update=False):
        #TODO: move this method to a form
        datum['home_team'] = FootballTeam.objects.get_or_create(name=datum['home_team'])[0]
        datum['away_team'] = FootballTeam.objects.get_or_create(name=datum['away_team'])[0]

        if datum.get('referee') is not None:
            datum['referee'] = Referee.objects.get_or_create(name=datum['referee'])[0]
        try:
            # Handle the two possible date formats
            datum['match_date'] = datetime.datetime.strptime(datum['match_date'], '%d/%m/%y').date()
        except ValueError:
            datum['match_date'] = datetime.datetime.strptime(datum['match_date'], '%d/%m/%Y').date()

        if update:
            match = MatchResult.objects.filter(home_team=datum['home_team'],
                                               away_team=datum['away_team'],
                                               match_date=datum['match_date'])
            match.update(**datum)
            return match.get()

        return MatchResult(**datum)

    def bulk_create_from_api(self, api_name, start_year):
        consumer = APIConsumer.create(self, api_name + 'Consumer', start_year)
        with transaction.atomic():
            self.bulk_create([self.match_from_datum(datum) for datum in consumer.get_data()])

    def bulk_update_from_api(self, api_name, start_year):
        consumer = APIConsumer.create(self, api_name + 'Consumer', start_year)
        with transaction.atomic():
            for datum in consumer.get_data(update=True):
                self.match_from_datum(datum, update=True)


class MatchResult(models.Model):

    # REQUIRED FIELDS

    home_team = models.ForeignKey(FootballTeam, related_name='home_matches')
    away_team = models.ForeignKey(FootballTeam, related_name='away_matches')
    referee = models.ForeignKey(Referee, null=True, blank=True)

    match_date = models.DateField()
    season_start_year = models.PositiveIntegerField()

    home_goals = models.PositiveSmallIntegerField()
    away_goals = models.PositiveSmallIntegerField()

    # END OF REQUIRED FIELDS

    def get_final_score(self):
        return (self.home_goals, self.away_goals)

    # ADDITIONAL MATCH STATISTICS

    attendance = models.PositiveIntegerField(null=True, blank=True)

    home_half_time_goals = models.PositiveSmallIntegerField(null=True, blank=True)
    away_half_time_goals = models.PositiveSmallIntegerField(null=True, blank=True)

    home_shots = models.PositiveSmallIntegerField(null=True, blank=True)
    away_shots = models.PositiveSmallIntegerField(null=True, blank=True)

    home_shots_on_target = models.PositiveSmallIntegerField(null=True, blank=True)
    away_shots_on_target = models.PositiveSmallIntegerField(null=True, blank=True)

    home_hit_woodwork = models.PositiveSmallIntegerField(null=True, blank=True)
    away_hit_woodwork = models.PositiveSmallIntegerField(null=True, blank=True)

    home_corners = models.PositiveSmallIntegerField(null=True, blank=True)
    away_corners = models.PositiveSmallIntegerField(null=True, blank=True)

    home_fouls = models.PositiveSmallIntegerField(null=True, blank=True)
    away_fouls = models.PositiveSmallIntegerField(null=True, blank=True)

    home_offsides = models.PositiveSmallIntegerField(null=True, blank=True)
    away_offsides = models.PositiveSmallIntegerField(null=True, blank=True)

    home_yellow_cards = models.PositiveSmallIntegerField(null=True, blank=True)
    away_yellow_cards = models.PositiveSmallIntegerField(null=True, blank=True)

    home_red_cards = models.PositiveSmallIntegerField(null=True, blank=True)
    away_red_cards = models.PositiveSmallIntegerField(null=True, blank=True)

    # END OF ADDITIONAL MATCH STATISTICS

    # MATCH BETTING ODDS

    bet365_home_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    bet365_draw = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    bet365_away_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    blue_square_home_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    blue_square_draw = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    blue_square_away_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    bet_and_win_home_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    bet_and_win_draw = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    bet_and_win_away_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    gamebookers_home_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    gamebookers_draw = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    gamebookers_away_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    interwetten_home_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    interwetten_draw = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    interwetten_away_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    ladbrokes_home_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    ladbrokes_draw = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    ladbrokes_away_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    pinnacle_sports_home_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    pinnacle_sports_draw = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    pinnacle_sports_away_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    sporting_odds_home_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sporting_odds_draw = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sporting_odds_away_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    sportingbet_home_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sportingbet_draw = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sportingbet_away_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    stan_james_home_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    stan_james_draw = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    stan_james_away_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    stanleybet_home_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    stanleybet_draw = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    stanleybet_away_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    vc_bet_home_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    vc_bet_draw = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    vc_bet_away_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    william_hill_home_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    william_hill_draw = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    william_hill_away_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    betbrain_max_home_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    betbrain_average_home_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    betbrain_max_draw = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    betbrain_average_draw = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    betbrain_max_away_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    betbrain_average_away_win = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    # END OF MATCH BETTING ODDS

    # GOALS BETTINGS ODDS

    betbrain_max_gt2goals = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    betbrain_average_gt2goals = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    betbrain_max_lte2goals = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    betbrain_average_lte2goals = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    # END OF GOALS BETTINGS ODDS

    # ASIAN HANDICAP BETTING ODDS

    betbrain_home_handicap = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    betbrain_max_home_handicap = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    betbrain_average_home_handicap = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    betbrain_max_away_handicap = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    betbrain_average_away_handicap = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    # END OF ASIAN HANDICAP BETTING ODDS

    objects = MatchResultManager()

    def __str__(self):
        return self.home_team.name + ' v ' + self.away_team.name
