from django.db import models
from django.conf import settings


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

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата ответа',
    )

    def __str__(self):
        return f'Ответ на заявку №{self.request_id}'
