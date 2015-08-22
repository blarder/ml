from django.views.generic import ListView, DetailView

from .models import FootballTeam, MatchResult
from ml.lib.chart import Chart


class FootballTeamList(ListView):
    model = FootballTeam


class FootballTeamDetail(DetailView):
    model = FootballTeam

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_matches'] = self.object.recent_matches()
        context['chart_config_1'] = Chart(element_id='chart1')
        context['chart_config_2'] = Chart(element_id='chart2')
        return context


class MatchResultList(ListView):
    model = MatchResult


class MatchResultDetail(DetailView):
    model = MatchResult
    queryset = MatchResult.objects.select_related('home_team', 'away_team')
