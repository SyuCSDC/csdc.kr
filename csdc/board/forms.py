from django import forms
from .models import Board , Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content']
    
    def __init__(self, *args, **kwargs):
        super(BoardForm, self).__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'id': 'summernote'})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('board', 'type' , 'commenter' )


