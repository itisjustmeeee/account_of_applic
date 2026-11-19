from django import forms
from django.contrib.auth import get_user_model

from .models import UserRequest
from category.models import Category
from statuses.models import RequestStatus

User = get_user_model()


class AttachmentSizeLimitMixin:
    def clean_attachment(self):
        uploaded_file = self.files.get(
            self.add_prefix('attachment')
        )

        if uploaded_file and uploaded_file.size > 20 * 1024 * 1024:
            raise forms.ValidationError(
                'Размер файла не должен превышать 20 МБ.'
            )


class RequestFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=100,
        strip=True,
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


class UserRequestCreateForm(AttachmentSizeLimitMixin, forms.ModelForm):
    class Meta:
        model = UserRequest

        fields = [
            'user',
            'category',
            'description',
            'priority',
            'attachment',
        ]

        labels = {
            'user': 'Пользователь',
            'category': 'Категория',
            'description': 'Описание проблемы',
            'priority': 'Приоритет проблемы',
            'attachment': 'Прикрепить файл (необязательно)',
        }

        widgets = {
            'user': forms.Select(),

            'category': forms.Select(),

            'description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Опишите, что вас беспокоит...',
            }),

            'priority': forms.Select(),

            'attachment': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg,.jpeg,.docx',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['user'].queryset = (
            User.objects
            .filter(is_active=True)
            .order_by('username')
        )
        self.fields['user'].empty_label = 'Выберите пользователя'

        self.fields['category'].queryset = (
            Category.objects.order_by('name')
        )
        self.fields['category'].empty_label = 'Выберите категорию'

        self.fields['attachment'].required = False
        self.fields['attachment'].empty_label = 'Выберите файл'


class UserRequestUpdateForm(AttachmentSizeLimitMixin, forms.ModelForm):
    class Meta:
        model = UserRequest
        fields = [
            'category',
            'description',
            'priority',
            'attachment',
        ]
        labels = {
            'category': 'Категория',
            'description': 'Описание проблемы',
            'priority': 'Приоритет пробелмы',
            'attachment': 'Прикрепить файл (необязательно)',
        },
        widgets = {
            'category': forms.Select(),
            'description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Опишите, что вас беспокоит...',
            }),
            'priority': forms.Select(),
            'attachment': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.png,.jpg,.jpeg,.docx',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].queryset = (
            Category.objects.order_by('name')
        )
        self.fields['category'].empty_label = 'Выберите категорию'

        self.fields['attachment'].required = False
        self.fields['attachment'].empty_label = 'Выберите файл'


class RequestStatusForm(forms.ModelForm):
    class Meta:
        model = UserRequest
        fields = ['status']
        labels = {
            'status': 'Статус заявки',
        }
        widgets = {
            'status': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['status'].queryset = (
            RequestStatus.objects.order_by('name')
        )
        self.fields['status'].empty_label = 'Выберите статус'
