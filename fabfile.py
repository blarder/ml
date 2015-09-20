from __future__ import with_statement
from os import path

from fabric.api import env, put, run, execute
from fabric.contrib.console import confirm
from fabric.network import disconnect_all

from fabric.contrib.django import settings_module
settings_module('config.settings.local')

from config.settings import secrets
from ml.lib import file_helpers
from jobs.models import MLJob


env.hosts = [secrets.arcus_domain]
env.user = secrets.arcus_username
env.password = secrets.arcus_password


def deploy_job_by_id(job_id):
    """
    Deploys a created job (using its id) to ARC.
    :param job_id: the job's id
    :return:
    """
    ml_job = MLJob.objects.get(id=job_id)
    overwrite_script = not confirm('script detected - keep current script?', default=True)

    _deploy_job(ml_job, overwrite_script=overwrite_script)


def _deploy_job(ml_job, overwrite_script=False):
    """
    Deploys a created job to ARC
    :param ml_job: the job to be deployed
    :param overwrite_script: whether a new script should be rendered, should one already exist
    :return:
    """

    if not file_helpers.script_exists(ml_job) or overwrite_script:
        file_helpers.create_script(ml_job)

    put_job_files(ml_job)

    arc_job_id = queue_job(ml_job)

    return arc_job_id


def deploy_job(*args, **kwargs):
    try:
        return execute(lambda: _deploy_job(*args, **kwargs), hosts=env.hosts)
    finally:
        disconnect_all()


def put_job_files(ml_job):
    run('mkdir -p {}'.format(ml_job.remote_directory))
    put(ml_job.local_directory, path.abspath(path.join(ml_job.remote_directory, '..')))


def queue_job(ml_job):
    job_script_path = file_helpers.form_job_script_path(ml_job.directory_name)
    return run('qsub {}'.format(job_script_path))


def _collect_job(ml_job):
    """
    Collects the result files (if ready) from ARC, stores them, and updates the db.
    :param ml_job: the job whose files are to be collected
    :return:
    """


def collect_job(*args, **kwargs):
    try:
        return execute(lambda: _collect_job(*args, **kwargs), hosts=env.hosts)
    finally:
        disconnect_all()
