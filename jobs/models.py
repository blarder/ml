from datetime import datetime

from django.db import models

from ml.lib import file_helpers


class MLJob(models.Model):

    SCRIPT_TEMPLATES = (
        ('torque_job', 'Torque Job'),
    )

    NOT_DEPLOYED = 'n'
    DEPLOYED = 'd'
    COMPLETED = 'c'

    JOB_STATUSES = (
        (NOT_DEPLOYED, 'Not deployed'),
        (DEPLOYED, 'Deployed'),
        (COMPLETED, 'Completed'),
    )

    creation_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, default='job')
    directory_name = models.CharField(max_length=255, unique=True, validators=[file_helpers.validate_directory_name])
    local_directory = models.FilePathField()
    remote_directory = models.FilePathField()
    script_template = models.CharField(max_length=255, choices=SCRIPT_TEMPLATES, default='torque_job')

    nodes = models.PositiveSmallIntegerField(blank=True, default=1)
    processes_per_node = models.PositiveSmallIntegerField(blank=True, default=1)
    walltime = models.PositiveIntegerField(blank=True, default=360000)
    notification_email = models.EmailField(blank=True, default='brett.larder@st-hildas.ox.ac.uk')

    model_file_name = models.CharField(max_length=255, default='model.pkl')
    metadata_file_name = models.CharField(max_length=255, default='metadata.txt')

    job_status = models.CharField(max_length=1, default=NOT_DEPLOYED, choices=JOB_STATUSES)

    # fields populated after deploying to ARC
    deployment_time = models.DateTimeField(null=True, blank=True)

    # fields populated on collection from ARC
    collection_time = models.DateTimeField(null=True, blank=True)

    notes = models.TextField(blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        being_created = False
        if not self.pk:
            being_created = True

        super(MLJob, self).save(force_insert=force_insert, force_update=force_update,
                                using=using, update_fields=update_fields)

        if being_created:
            file_helpers.make_package(self)
            self.save()

    def delete(self, using=None):
        file_helpers.move_package_to_deleted(self)
        super(MLJob, self).delete(using=using)

    def was_deployed(self):
        self.deployment_time = datetime.now()
        self.job_status = self.DEPLOYED
        self.save()

    def was_collected(self):
        self.collection_time = datetime.now()
        self.job_status = self.COMPLETED
        self.save()

    def __str__(self):
        return self.directory_name
