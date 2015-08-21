__author__ = 'brett'
import io

import requests
import pandas


class APIConsumer(object):
    def get_data_for_season(self, season_start_year):
        raise NotImplementedError


class FootballDataConsumer(APIConsumer):

    url_format = 'http://www.football-data.co.uk/mmz4281/{}{}/E0.csv'

    #TODO: populate mapping dictionary from website
    column_mapping = dict(

    )

    def __init__(self, largest_seen_id=-1):
        super().__init__()
        self.largest_seen_id = largest_seen_id

    def get_data_for_season(self, start_year):
        url = self.url_format.format(start_year, start_year + 1)
        csv_string = requests.get(url).text
        data = pandas.read_csv(io.StringIO(csv_string))\
            .rename(columns=self.column_mapping)\
            .transpose()\
            .to_dict()

        #TODO: perform filtering/manipulation using pandas for large sets (rather than natively as follows)

        for match_id, match_data in data.items():
            if match_data > self.largest_seen_id:
                match_data['season_id'] = match_id
                yield match_data
