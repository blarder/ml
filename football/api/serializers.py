__author__ = 'brett'
from rest_framework import serializers

from ..models import MatchResult


class MatchResultSerializer(serializers.ModelSerializer):

    home_team = serializers.StringRelatedField()
    away_team = serializers.StringRelatedField()

    class Meta:
        model = MatchResult
        fields = ('home_team', 'away_team', 'home_goals', 'away_goals', 'match_date')
