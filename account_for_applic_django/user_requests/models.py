from django.db import models
from django.conf import settings

from category.models import Category
from statuses.models import RequestStatus


class UserRequest(models.Model):

    PRIORITY_CHOICES = [
        ('Низкий', 'Низкий'),
        ('Средний', 'Средний'),
        ('Высокий', 'Высокий'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='requests',
        verbose_name='Пользователь'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='requests',
        verbose_name='Категория'
    )

    status = models.ForeignKey(
        RequestStatus,
        on_delete=models.PROTECT,
        related_name='requests',
        verbose_name='Статус'
    )

    description = models.TextField(
        verbose_name='Описание'
    )

    priority = models.CharField(
        max_length=25,
        choices=PRIORITY_CHOICES,
        default='Средний',
        verbose_name='Приоритет',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'Заявка №{self.id}'
