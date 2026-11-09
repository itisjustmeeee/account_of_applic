from django.db import models
from django.db.models import Case, When, Value
from django.conf import settings

from category.models import Category
from statuses.models import RequestStatus

from django.urls import reverse


class UserRequest(models.Model):

    def get_absolute_url(self):
        return reverse(
            'user_requests:detail',
            kwargs={'request_id': self.pk}
        )

    class Priority(models.TextChoices):
        LOW = 'low', 'Низкий'
        MEDIUM = 'medium', 'Средний'
        HIGH = 'high', 'Высокий'

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
        choices=Priority.choices,
        default=Priority.MEDIUM,
        verbose_name='Приоритет',
    )

    priority_number = models.GeneratedField(
        expression=Case(
            When(
                priority=Priority.LOW,
                then=Value(1),
            ),
            When(
                priority=Priority.MEDIUM,
                then=Value(2),
            ),
            When(
                priority=Priority.HIGH,
                then=Value(3),
            ),
            output_field=models.IntegerField(),
        ),
        output_field=models.IntegerField(),
        db_persist=False,
        verbose_name='Числовой приоритет',
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
