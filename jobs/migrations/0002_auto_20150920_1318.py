# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mljob',
            name='ml_model',
        ),
        migrations.AddField(
            model_name='mljob',
            name='metadata_file_name',
            field=models.CharField(default=b'metadata.txt', max_length=255),
        ),
        migrations.AddField(
            model_name='mljob',
            name='model_file_name',
            field=models.CharField(default=b'model.pkl', max_length=255),
        ),
        migrations.AddField(
            model_name='mljob',
            name='notes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='MLModel',
        ),
    ]
