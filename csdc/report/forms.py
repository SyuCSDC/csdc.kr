
from django import forms
from django.forms import modelformset_factory
from django.core.exceptions import ValidationError
from .models import Report, ReportFile , Book

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['book']  # submitter는 뷰에서 처리
    
    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields['book'].label = ''
        self.fields['book'].empty_label = '책을 선택해주세요.'
        self.fields['book'].widget.attrs.update({'class': 'form-select'})


class ReportFileForm(forms.ModelForm):
    class Meta:
        model = ReportFile
        fields = ('file',)

    def __init__(self, *args, **kwargs):
        super(ReportFileForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({'class': 'form-control'})


ReportFileFormSet = modelformset_factory(
    ReportFile,
    form=ReportFileForm,
    fields=('file',),
    extra=5,
    can_delete=True,
)

class BookRequestForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'needed_copies' , ]

    def clean(self):
        cleaned_data = super().clean()
        needed_copies = cleaned_data.get('needed_copies')

        if needed_copies is not None and needed_copies <= 0:
            # 필드별 에러 메시지 추가
            self.add_error('needed_copies', '수량은 0보다 커야 합니다.')
        
        return cleaned_data



