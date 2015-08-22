__author__ = 'brett'
from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^teams/$',
        view=views.FootballTeamList.as_view(),
        name='team_list'
    ),

    # URL pattern for the UserDetailView
    url(
        regex=r'^teams/(?P<pk>[0-9]+)/$',
        view=views.FootballTeamDetail.as_view(),
        name='team_detail'
    ),

]
