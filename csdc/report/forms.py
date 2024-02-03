
from django import forms
from django.forms import modelformset_factory
from .models import Report, ReportFile

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['book']  # submitter는 뷰에서 처리

ReportFileFormSet = modelformset_factory(
    ReportFile,
    fields=('file',),
    extra=1,
    can_delete=True
)
