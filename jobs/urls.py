# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^deploy/$',
        view=views.deploy,
        name='deploy'
    ),

    url(
        regex=r'^collect/$',
        view=views.collect,
        name='collect'
    ),
]
