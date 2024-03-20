from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Board , Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content']
    
    def __init__(self, *args, **kwargs):
        super(BoardForm, self).__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs['maxlength'] = 50
        self.fields['content'].widget.attrs.update({'id': 'summernote'})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('board', 'type' , 'commenter' )
        fiedls = ['content']
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'comment',
        'placeholder': '댓글을 입력하세요.',
        'rows': 1,
    }))
      

