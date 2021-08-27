from django.forms import ModelForm, TextInput
from categorylist.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите название',
                'id': 'floatingName'
            })
        }