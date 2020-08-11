from django import forms
from .models import UsedComment, UsedProduct, UsedCategory, UsedSubCategory


class CommentForm(forms.ModelForm):
    class Meta:
        model = UsedComment
        fields = ['content', ]


class UsedProductForm(forms.ModelForm):
    image = forms.ImageField(required=True, widget=forms.TextInput(attrs={
        'accept': "image/x-png,image/gif,image/jpeg"
    })
    )

    class Meta:
        model = UsedProduct
        fields = ['title', 'author', 'price',
                  'description', 'image']
