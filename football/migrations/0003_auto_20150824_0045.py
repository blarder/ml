# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0002_auto_20150823_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchresult',
            name='attendance',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='away_corners',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='away_fouls',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='away_hit_woodwork',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='away_offsides',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='away_red_cards',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='away_shots',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='away_shots_on_target',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='away_yellow_cards',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='bet365_away_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='bet365_draw',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='bet365_home_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='bet_and_win_away_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='bet_and_win_draw',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='bet_and_win_home_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='betbrain_average_away_handicap',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='betbrain_average_away_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='betbrain_average_draw',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='betbrain_average_gt2goals',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='betbrain_average_home_handicap',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='betbrain_average_home_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='betbrain_average_lte2goals',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='betbrain_home_handicap',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='betbrain_max_away_handicap',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='betbrain_max_away_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='betbrain_max_draw',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='betbrain_max_gt2goals',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='betbrain_max_home_handicap',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='betbrain_max_home_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='betbrain_max_lte2goals',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='blue_square_away_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='blue_square_draw',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='blue_square_home_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='gamebookers_away_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='gamebookers_draw',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='gamebookers_home_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='home_corners',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='home_fouls',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='home_hit_woodwork',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='home_offsides',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='home_red_cards',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='home_shots',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='home_shots_on_target',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='home_yellow_cards',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='interwetten_away_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='interwetten_draw',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='interwetten_home_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='ladbrokes_away_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='ladbrokes_draw',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='ladbrokes_home_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='pinnacle_sports_away_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='pinnacle_sports_draw',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='pinnacle_sports_home_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='referee',
            field=models.ForeignKey(null=True, blank=True, to='football.Referee'),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='sporting_odds_away_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='sporting_odds_draw',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='sporting_odds_home_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='sportingbet_away_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='sportingbet_draw',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='sportingbet_home_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='stan_james_away_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='stan_james_draw',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='stan_james_home_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='stanleybet_away_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='stanleybet_draw',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='stanleybet_home_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='vc_bet_away_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='vc_bet_draw',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='vc_bet_home_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='william_hill_away_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='william_hill_draw',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AddField(
            model_name='matchresult',
            name='william_hill_home_win',
            field=models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='matchresult',
            name='away_half_time_goals',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='matchresult',
            name='home_half_time_goals',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
    ]
