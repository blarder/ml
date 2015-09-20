from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset


class DeployForm(forms.Form):

    overwrite_script = forms.BooleanField(
        label='Overwrite job script (if present)?',
        initial=False,
        required=True
    )

    job_id = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=True
    )

    def __init__(self, job_id, *args, **kwargs):
        super(DeployForm, self).__init__(*args, **kwargs)
        self.fields['job_id'].initial = job_id
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'jobs:deploy'

        self.helper.layout = Layout(
            Fieldset(
                'Deployment',
                'overwrite_script',
                'job_id',
                Submit('submit', 'Deploy job to ARC')
            ),
        )


class CollectForm(forms.Form):

    job_id = forms.IntegerField(
        widget=forms.HiddenInput(),
        required=True
    )

    def __init__(self, job_id, *args, **kwargs):
        super(CollectForm, self).__init__(*args, **kwargs)
        self.fields['job_id'].initial = job_id
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'jobs:collect'

        self.helper.layout = Layout(
            Fieldset(
                'Collection',
                'job_id',
                Submit('submit', 'Collect data from ARC')
            ),
        )
