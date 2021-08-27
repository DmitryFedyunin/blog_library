from .models import Materials
from django.forms import ModelForm, TextInput, Textarea

class MaterialsForm(ModelForm):
    class Meta:
        model = Materials
        fields = ['title','type', 'author','category', 'description']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите название',
                'id': 'floatingName'
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите авторов',
                'id': 'floatingAuthor'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите краткое описание',
                'id': 'floatingDescription'
            }),
            'category': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите категорию',
                'id': 'floatingSelectCategory'
            }),
            'type': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите тип',
                'id': 'floatingSelectType'
            }),
        }
