from django.forms import ModelForm, TextInput
from tagslist.models import Tags


class TagsForm(ModelForm):
    class Meta:
        model = Tags
        fields = ['title']

        widgets ={
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите название',
                'id': 'floatingName'
            })
        }