from django import forms
from .models import UsedComment, UsedProduct, UsedCategory, UsedSubCategory


class CommentForm(forms.ModelForm):
    class Meta:
        model = UsedComment
        fields = ['content', ]


# choices = UsedSubCategory.objects.all().values_list('name', 'name')


class UsedProductForm(forms.ModelForm):
    # subcategory = forms.Select(choices=choices)

    class Meta:
        model = UsedProduct
        fields = ['title', 'author', 'price',
                  'description', 'image']

    def __init__(self, request, *args, **kwargs):
        super(UsedProductForm, self).__init__(*args, **kwargs)
        self.fields['subcategory'] = forms.CharField(
            label='', max_length=100, initial=request.session['value'])
