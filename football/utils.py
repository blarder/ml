__author__ = 'brett'
from .models import MatchResult


def populate_db():
    for year in range(1993, 2016):
        MatchResult.objects.bulk_create_from_api('FootballData', year)
        print('Parsed year {}'.format(year))

def update_db():
    for year in range(1993, 2016):
        MatchResult.objects.bulk_update_from_api('FootballData', year)
        print('Updated year {}'.format(year))
