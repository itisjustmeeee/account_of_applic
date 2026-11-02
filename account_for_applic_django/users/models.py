from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('user', 'Пользователь'),
        ('admin', 'Администратор')
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Пользователь'
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='user',
        verbose_name='Роль',
    )

    def __str__(self):
        return f'{self.user.username} - {self.get_role_display()}'
