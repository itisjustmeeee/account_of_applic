from django.db import models


class RequestStatus(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Название',
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name
