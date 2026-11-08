from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        labels = {
            'name': 'Название категории',
            'description': 'Описание категории',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Введите название категории',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Введите описание категории',
                'rows': 4,
            }),
        }
