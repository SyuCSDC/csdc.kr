
from django import forms
from django.forms import modelformset_factory
from .models import Report, ReportFile , Book

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['book']  # submitter는 뷰에서 처리

ReportFileFormSet = modelformset_factory(
    ReportFile,
    fields=('file',),
    extra=5,
    can_delete=True
)


class BookRequestForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'needed_copies' , ]



