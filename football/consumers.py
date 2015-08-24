__author__ = 'brett'
import io
import re

import requests
import pandas


class APIConsumer(object):
    """
    Base interface for classes that extract data from REST APIs to populate database
    """
    def __init__(self, manager, start_year):
        self.manager = manager
        self.start_year = start_year

    def get_data(self):
        raise NotImplementedError

    @classmethod
    def create(cls, manager, class_name, start_year):
        for subclass in cls.__subclasses__():
            if subclass.__name__ == class_name:
                return subclass(manager, start_year)

        raise LookupError('No registered APIConsumer has the requested name "{}"'.format(class_name))


class FootballDataConsumer(APIConsumer):
    """
    API consumer for football-data.co.uk
    """

    url_format = 'http://www.football-data.co.uk/mmz4281/{}{}/E0.csv'
    bad_line_end = re.compile('(,+)\r\n')

    #TODO: populate mapping dictionary from website
    column_mapping = {
        'HomeTeam': 'home_team',
        'AwayTeam': 'away_team',
        'FTHG': 'home_goals',
        'FTAG': 'away_goals',
        'Date': 'match_date',
        'HTHG': 'home_half_time_goals',
        'HTAG': 'away_half_time_goals',
        'Attendance': 'attendance',
        'Referee': 'referee',
        'HS': 'home_shots',
        'AS': 'away_shots',
        'HST': 'home_shots_on_target',
        'AST': 'away_shots_on_target',
        'HHW': 'home_hit_woodwork',
        'AHW': 'away_hit_woodwork',
        'HC': 'home_corners',
        'AC': 'away_corners',
        'HF': 'home_fouls',
        'AF': 'away_fouls',
        'HO': 'home_offsides',
        'AO': 'away_offsides',
        'HY': 'home_yellow_cards',
        'AY': 'away_yellow_cards',
        'HR': 'home_red_cards',
        'AR': 'away_red_cards',

        'B365H': 'bet365_home_win',
        'B365D': 'bet365_draw',
        'B365A': 'bet365_away_win',

        'BSH': 'blue_square_home_win',
        'BSD': 'blue_square_draw',
        'BSA': 'blue_square_away_win',

        'BWH': 'bet_and_win_home_win',
        'BWD': 'bet_and_win_draw',
        'BWA': 'bet_and_win_away_win',

        'GBH': 'gamebookers_home_win',
        'GBD': 'gamebookers_draw',
        'GBA': 'gamebookers_away_win',

        'IWH': 'interwetten_home_win',
        'IWD': 'interwetten_draw',
        'IWA': 'interwetten_away_win',

        'LBH': 'ladbrokes_home_win',
        'LBD': 'ladbrokes_draw',
        'LBA': 'ladbrokes_away_win',

        'PSH': 'pinnacle_sports_home_win',
        'PSD': 'pinnacle_sports_draw',
        'PSA': 'pinnacle_sports_away_win',

        'SOH': 'sporting_odds_home_win',
        'SOD': 'sporting_odds_draw',
        'SOA': 'sporting_odds_away_win',

        'SBH': 'sportingbet_home_win',
        'SBD': 'sportingbet_draw',
        'SBA': 'sportingbet_away_win',

        'SJH': 'stan_james_home_win',
        'SJD': 'stan_james_draw',
        'SJA': 'stan_james_away_win',

        'SYH': 'stanleybet_home_win',
        'SYD': 'stanleybet_draw',
        'SYA': 'stanleybet_away_win',

        'VCH': 'vc_bet_home_win',
        'VCD': 'vc_bet_draw',
        'VCA': 'vc_bet_away_win',

        'WHH': 'william_hill_home_win',
        'WHD': 'william_hill_draw',
        'WHA': 'william_hill_away_win',

        'BbMxH': 'betbrain_max_home_win',
        'BbAvH': 'betbrain_average_home_win',
        'BbMxD': 'betbrain_max_draw',
        'BbAvD': 'betbrain_average_draw',
        'BbMxA': 'betbrain_max_away_win',
        'BbAvA': 'betbrain_average_away_win',

        'BbMx>2.5': 'betbrain_max_gt2goals',
        'BbAv>2.5': 'betbrain_average_gt2goals',
        'BbMx<2.5': 'betbrain_max_lte2goals',
        'BbAv<2.5': 'betbrain_average_lte2goals',

        'BbAHh': 'betbrain_home_handicap',
        'BbMxAHH': 'betbrain_max_home_handicap',
        'BbAvAHH': 'betbrain_average_home_handicap',
        'BbMxAHA': 'betbrain_max_away_handicap',
        'BbAvAHA': 'betbrain_average_away_handicap'

    }

    def clean_string(self, string):
        """
        Removes trailing columns from rows, so that the pandas parser can handle the data
        :param string:
        :return:
        """
        return self.bad_line_end.sub('\r\n', string)

    def get_data(self, update=False):
        url = self.url_format.format(str(self.start_year)[-2:], str(self.start_year + 1)[-2:])
        csv_string = self.clean_string(requests.get(url).text)
        dataframe = pandas.read_csv(io.StringIO(csv_string))\
            .filter(items=self.column_mapping.keys())\
            .rename(columns=self.column_mapping)\
            .transpose()

        data = dataframe.where((pandas.notnull(dataframe)), None).to_dict()

        #TODO: perform filtering/manipulation using pandas for large sets (rather than natively as follows)

        largest_seen_id = self.manager.filter(season_start_year=self.start_year).count() - 1

        for match_id, match_data in data.items():
            if match_id <= largest_seen_id and not update or match_data['home_goals'] is None:
                continue
            match_data['season_start_year'] = self.start_year
            print(match_data)
            yield match_data
