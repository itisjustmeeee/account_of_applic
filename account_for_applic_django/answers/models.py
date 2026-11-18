from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator


class Answer(models.Model):
    request = models.OneToOneField(
        'user_requests.UserRequest',
        on_delete=models.CASCADE,
        related_name='answer_record',
        verbose_name='Заявка',
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='written_answers',
        verbose_name='Автор ответа',
        null=True,
        blank=True,
    )

    text = models.TextField(
        verbose_name='Текст ответа'
    )

    attachment = models.FileField(
        upload_to='answer_attachments/%Y/%m/',
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf', 'png', 'jpg', 'jpeg', 'docx']
            )
        ],
        verbose_name='Вложение',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата ответа',
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return f'Ответ на заявку №{self.request_id}'
