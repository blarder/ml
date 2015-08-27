__author__ = 'brett'
from django.conf.urls import url, include

from rest_framework import routers

from . import views
from .api import views as api_views


api_router = routers.SimpleRouter()
api_router.register('matches', api_views.MatchResultViewSet, base_name='matches')


urlpatterns = [

    url(r'^api/', include(api_router.urls, namespace='api')),

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

    url(
        regex=r'^seasons/$',
        view=views.SeasonList.as_view(),
        name='season_list'
    ),

    url(
        regex=r'^seasons/(?P<pk>[0-9]+)/$',
        view=views.SeasonDetail.as_view(),
        name='season_detail'
    ),

]
