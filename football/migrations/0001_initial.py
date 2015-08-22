# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FootballTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MatchResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('match_date', models.DateField()),
                ('season_start_year', models.PositiveIntegerField()),
                ('home_goals', models.PositiveSmallIntegerField()),
                ('away_goals', models.PositiveSmallIntegerField()),
                ('away_team', models.ForeignKey(related_name='away_matches', to='football.FootballTeam')),
                ('home_team', models.ForeignKey(related_name='home_matches', to='football.FootballTeam')),
            ],
        ),
    ]
