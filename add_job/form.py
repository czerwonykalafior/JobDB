from django import forms

import add_job.views
from .models import Job
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Fieldset, HTML, Row
from crispy_forms.bootstrap import FormActions
from django.core.urlresolvers import reverse

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('stanowisko', 'branze', 'opis', 'tags',)
