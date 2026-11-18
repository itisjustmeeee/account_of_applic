from django import forms
from django.contrib.auth import get_user_model

from .models import Answer
from user_requests.forms import AttachmentSizeLimitMixin

User = get_user_model()


class AnswerCreateForm(AttachmentSizeLimitMixin, forms.ModelForm):

    author = forms.ModelChoiceField(
        queryset=User.objects.none(),
        label='Автор ответа',
        empty_label='Выберите администратора',
    )

    class Meta:
        model = Answer

        fields = [
            'author',
            'text',
            'attachment',
        ]

        labels = {
            'author': 'Кто добавляет ответ',
            'text': 'Текст ответа на заявку',
            'attachment': 'Прикрепить файл (необязательно)',
        }

        widgets = {
            'author': forms.Select(),

            'text': forms.Textarea(attrs={
                'rows': 6,
                'placeholder': 'Введите ответ...'
            }),
            'attachment': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg,.jpeg,.docx',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].queryset = (
            User.objects
            .filter(
                is_active=True,
                profile__role='admin',
            )
            .order_by('username')
        )

        self.fields['attachment'].required = False
        self.fields['attachment'].empty_label = 'Выберите файл'
