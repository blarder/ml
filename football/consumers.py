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
        'Date': 'match_date'
    }

    def clean_string(self, string):
        """
        Removes trailing columns from rows, so that the pandas parser can handle the data
        :param string:
        :return:
        """
        return self.bad_line_end.sub('\r\n', string)

    def get_data(self):
        url = self.url_format.format(str(self.start_year)[-2:], str(self.start_year + 1)[-2:])
        csv_string = self.clean_string(requests.get(url).text)
        data = pandas.read_csv(io.StringIO(csv_string))[list(self.column_mapping.keys())]\
            .rename(columns=self.column_mapping)\
            .transpose()\
            .to_dict()

        #TODO: perform filtering/manipulation using pandas for large sets (rather than natively as follows)

        largest_seen_id = self.manager.filter(season_start_year=self.start_year).count()

        for match_id, match_data in data.items():
            if match_id > largest_seen_id:
                match_data['season_start_year'] = self.start_year
                yield match_data
