# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ml.lib.file_helpers


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MLJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archived', models.BooleanField(default=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default=b'job', max_length=255)),
                ('directory_name', models.CharField(unique=True, max_length=255, validators=[ml.lib.file_helpers.validate_directory_name])),
                ('local_directory', models.FilePathField()),
                ('remote_directory', models.FilePathField()),
                ('script_template', models.CharField(default=b'torque_job', max_length=255, choices=[(b'torque_job', b'Torque Job')])),
                ('nodes', models.PositiveSmallIntegerField(default=1, blank=True)),
                ('processes_per_node', models.PositiveSmallIntegerField(default=1, blank=True)),
                ('walltime', models.PositiveIntegerField(default=360000, blank=True)),
                ('notification_email', models.EmailField(default=b'brett.larder@st-hildas.ox.ac.uk', max_length=254, blank=True)),
                ('deployment_time', models.DateTimeField(null=True, blank=True)),
                ('collection_time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MLModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('model_file_path', models.FilePathField()),
            ],
        ),
        migrations.AddField(
            model_name='mljob',
            name='ml_model',
            field=models.ForeignKey(blank=True, to='jobs.MLModel', null=True),
        ),
    ]
