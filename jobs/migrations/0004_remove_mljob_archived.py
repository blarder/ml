# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20150920_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mljob',
            name='archived',
        ),
    ]
