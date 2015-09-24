# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20150920_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mljob',
            name='script_template',
            field=models.CharField(default=b'anaconda_job', max_length=255, choices=[(b'python3_job', b'Python 3 Job'), (b'anaconda_job', b'Anaconda Job')]),
        ),
    ]
