__author__ = 'brett'
from rest_framework import viewsets, exceptions

from ..models import MatchResult
from .serializers import MatchResultSerializer


class MatchResultViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = MatchResult.objects.all().select_related('home_team', 'away_team')

    def get_queryset(self):
        try:
            return self.queryset.filter(season_start_year=self.request.query_params['season']).order_by('match_date')
        except (KeyError, ValueError):
            raise exceptions.ParseError('season parameter (with a valid year in which a season began) is required')

    serializer_class = MatchResultSerializer
