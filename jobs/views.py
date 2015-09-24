from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from fabfile import deploy_job, collect_job

from .models import MLJob


@staff_member_required
@require_POST
def deploy(request):
    job_id = request.POST['job_id']
    overwrite = request.POST.get('overwrite_script') == 'on'
    job = MLJob.objects.get(id=job_id)

    arc_job_id = deploy_job(job, overwrite_script=overwrite).values()[0]

    print('job queued with id {}'.format(arc_job_id))
    job.was_deployed()

    return HttpResponseRedirect(reverse('admin:jobs_mljob_change', args=(job_id,)))


@staff_member_required
@require_POST
def collect(request):
    job_id = request.POST['job_id']
    job = MLJob.objects.get(id=job_id)

    collected = collect_job(job).values()[0]

    if collected:
        job.was_collected()

    return HttpResponseRedirect(reverse('admin:jobs_mljob_change', args=(request.POST['job_id'],)))
