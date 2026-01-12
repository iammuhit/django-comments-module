from django import forms

from mayacms.contrib.comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model  = Comment
        fields = [
            'author',
            'comment',
        ]

        widgets = {
            'author' : forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
