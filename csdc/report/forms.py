
from django import forms
from django.forms import modelformset_factory
from .models import Report, ReportFile , Book

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['book']  # submitter는 뷰에서 처리


class ReportFileForm(forms.ModelForm):
    class Meta:
        model = ReportFile
        fields = ('file',)

    def __init__(self, *args, **kwargs):
        super(ReportFileForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({'class': 'minseong'})


ReportFileFormSet = modelformset_factory(
    ReportFile,
    form=ReportFileForm,
    fields=('file',),
    extra=5,
    can_delete=True
)

class BookRequestForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'needed_copies' , ]



