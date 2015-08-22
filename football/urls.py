__author__ = 'brett'
from django.conf.urls import url

from . import views

urlpatterns = [

    url(
        regex=r'^teams/$',
        view=views.FootballTeamList.as_view(),
        name='team_list'
    ),

    url(
        regex=r'^teams/(?P<pk>[0-9]+)/$',
        view=views.FootballTeamDetail.as_view(),
        name='team_detail'
    ),

    url(
        regex=r'^matches/$',
        view=views.MatchResultList.as_view(),
        name='match_list'
    ),

    url(
        regex=r'^matches/(?P<pk>[0-9]+)/$',
        view=views.MatchResultDetail.as_view(),
        name='match_detail'
    ),

]
