from django import forms
from .models import UsedComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = UsedComment
        fields = ['content', ]
