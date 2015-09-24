from __future__ import with_statement
from os import path

from fabric.api import env, put, run, execute, get
from fabric.contrib.console import confirm
from fabric.contrib.files import exists
from fabric.network import disconnect_all

from fabric.contrib.django import settings_module
settings_module('config.settings.local')

from config.settings import secrets
from ml.lib import file_helpers
from jobs.models import MLJob


env.hosts = [secrets.arcus_domain]
env.user = secrets.arcus_username
env.password = secrets.arcus_password

# TODO: change jobs directory so that it can be .gitignored

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
    :return: the id of the job on ARC
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
    if not exists(path.join(ml_job.remote_directory, ml_job.model_file_name)):
        print('Job output files not present - job is incomplete or failed')
        return False

    get(path.join(ml_job.remote_directory, ml_job.model_file_name) + '*',
        ml_job.local_directory)

    get(path.join(ml_job.remote_directory, ml_job.metadata_file_name),
        path.join(ml_job.local_directory, ml_job.metadata_file_name))

    return True


def collect_job(*args, **kwargs):
    try:
        return execute(lambda: _collect_job(*args, **kwargs), hosts=env.hosts)
    finally:
        disconnect_all()


def install_python3():
    transfer_python3_tgz()


def transfer_python3_tgz():
    put(file_helpers.form_python3_tgz_path(), path.join(secrets.arcus_home_path, 'local'))


def create_script(directory_name):
    job = MLJob.objects.get(directory_name=directory_name)
    file_helpers.create_script(job)
