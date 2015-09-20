# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20150920_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='mljob',
            name='job_status',
            field=models.CharField(default=b'n', max_length=1, choices=[(b'n', b'Not deployed'), (b'd', b'Deployed'), (b'c', b'Completed')]),
        ),
        migrations.AlterField(
            model_name='mljob',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
