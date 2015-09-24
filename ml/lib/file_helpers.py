from __future__ import with_statement
from os import path, mkdir
import shutil
from datetime import datetime

from django.template.loader import render_to_string
from django.core.exceptions import ValidationError

from config.settings import secrets


def form_dir_path(directory_name):
    return path.abspath(path.join(path.dirname(path.realpath(__file__)), '..', '..', 'current_jobs', directory_name))


def form_deleted_dir_path(directory_name):
    mangled_dir_name = directory_name + '_' + str(datetime.now())\
        .replace('-', '')\
        .replace('.', '')\
        .replace(' ', '')\
        .replace(':', '')

    return path.abspath(path.join(path.dirname(path.realpath(__file__)), '..', '..', 'deleted_jobs', mangled_dir_name))


def validate_directory_name(directory_name):
    # TODO: validate at database level rather than file level - always create/delete the files after
    # performing the corresponding database update

    dir_path = form_dir_path(directory_name)

    if path.exists(dir_path):
        raise ValidationError('Directory or file with this name "{}" exists'.format(dir_path))

    return directory_name


def form_remote_dir_path(directory_name):
    return path.join(secrets.arcus_data_path, 'jobs', directory_name)


def form_job_script_path(directory_name):
    return path.join(form_remote_dir_path(directory_name), 'job.sh')


def form_python3_tgz_path():
    return path.join(path.dirname(path.realpath(__file__)), 'Python-3.4.3.tgz')


def make_package(ml_job):
    ml_job.local_directory = form_dir_path(ml_job.directory_name)
    mkdir(ml_job.local_directory)

    package_path = path.join(ml_job.local_directory, ml_job.name)
    mkdir(package_path)

    requirements_path = path.join(package_path, 'requirements.txt')

    ml_job.remote_directory = form_remote_dir_path(ml_job.directory_name)

    with open(requirements_path, 'w') as f:
        f.write(render_to_string('requirements', {}))

    open(path.join(package_path, '__init__.py'), 'w').close()

    with open(path.join(package_path, '__main__.py'), 'w') as f:
        f.write(render_to_string('python_main.py', {}))


def move_package_to_deleted(ml_job):
    shutil.move(ml_job.local_directory, form_deleted_dir_path(ml_job.directory_name))


def script_exists(ml_job):
    script_path = path.join(ml_job.local_directory, 'job.sh')
    return path.exists(script_path)


def create_script(ml_job):
    ml_job.remote_package_path = path.join(ml_job.remote_directory, ml_job.name)
    ml_job.remote_requirements_path = path.join(ml_job.remote_package_path, 'requirements.txt')

    ml_job.model_output_path = path.join(ml_job.remote_directory, ml_job.model_file_name)
    ml_job.metadata_output_path = path.join(ml_job.remote_directory, ml_job.metadata_file_name)

    m, s = divmod(ml_job.walltime, 60)
    h, m = divmod(m, 60)
    ml_job.formatted_walltime = "%d:%02d:%02d" % (h, m, s)

    with open(path.join(ml_job.local_directory, 'job.sh'), 'w') as f:
        f.write(render_to_string(ml_job.script_template, ml_job.__dict__))
