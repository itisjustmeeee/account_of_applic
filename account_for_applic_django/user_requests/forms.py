from django import forms

from .models import UserRequest
from category.models import Category
from statuses.models import RequestStatus


class RequestFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        label='Поиск',
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите текст или ID заявки',
        }),
    )

    status = forms.ModelChoiceField(
        queryset=RequestStatus.objects.order_by('name'),
        required=False,
        label='Статус',
        empty_label='Все статусы',
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.order_by('name'),
        required=False,
        label='Категория',
        empty_label='Все категории',
    )

    priority = forms.ChoiceField(
        required=False,
        label='Приоритет',
        choices=[
            ('', 'Все приоритеты'),
            *UserRequest.Priority.choices,
        ],
    )

    unanswered_only = forms.BooleanField(
        required=False,
        label='Только заявки без ответа',
    )


class AnswerRequestFilterForm(RequestFilterForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields.pop('unanswered_only', None)
