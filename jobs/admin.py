from django.contrib import admin
from .models import MLJob
from .forms import DeployForm, CollectForm


@admin.register(MLJob)
class MLJobAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_time', 'local_directory', 'remote_directory',
                       'deployment_time', 'collection_time', 'job_status')

    list_display = ('directory_name', 'name', 'job_status', 'creation_time', 'deployment_time', 'collection_time')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['deploy_form'] = DeployForm(object_id)
        extra_context['collect_form'] = CollectForm(object_id)
        return super(MLJobAdmin, self).change_view(request, object_id=object_id,
                                                   form_url=form_url, extra_context=extra_context)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('directory_name',)
        return self.readonly_fields

    def get_actions(self, request):
        actions = super(MLJobAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
