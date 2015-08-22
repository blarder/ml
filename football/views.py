from django.views.generic import ListView, DetailView

from .models import FootballTeam, MatchResult


class FootballTeamList(ListView):
    model = FootballTeam


class FootballTeamDetail(DetailView):
    model = FootballTeam

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_matches'] = self.object.recent_matches()
        return context


class MatchResultList(ListView):
    model = MatchResult


class MatchResultDetail(DetailView):
    model = MatchResult
