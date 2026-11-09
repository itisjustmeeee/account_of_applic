from django.db import models
from django.conf import settings

from django.urls import reverse


class UserProfile(models.Model):

    def get_absolute_url(self):
        return reverse(
            "users:detail",
            kwargs={"user_id": self.pk}
        )

    class RoleChoises(models.TextChoices):
        USER = 'user', 'Пользователь'
        ADMIN = 'admin', 'Администратор'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Пользователь'
    )

    role = models.CharField(
        max_length=10,
        choices=RoleChoises.choices,
        default=RoleChoises.USER,
        verbose_name='Роль',
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.user.username} - {self.get_role_display()}'
