from django.db import models


class UserRequest(models.Model):
    STATUS_CHOICES = [
        ('Новая', 'Новая'),
        ('В работе', 'В работе'),
        ('Решена', 'Решена'),
    ]

    PRIORITY_CHOICES = [
        ('Низкий', 'Низкий'),
        ('Средний', 'Средний'),
        ('Высокий', 'Высокий'),
    ]

    user = models.CharField(
        max_length=100,
        verbose_name='Пользователь',
    )

    category = models.CharField(
        max_length=100,
        verbose_name='Категория',
    )

    description = models.TextField(
        max_length=100,
        verbose_name='Описание',
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Новая',
        verbose_name='Статус',
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='Средний',
        verbose_name='Приоритет',
    )

    answer = models.TextField(
        blank=True,
        default='',
        verbose_name='Ответ'
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
