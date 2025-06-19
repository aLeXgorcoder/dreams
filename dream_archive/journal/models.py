from django.db import models


class Dream(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Сон'
        verbose_name_plural = 'Сны'
        ordering = ['-date_created']

    def __str__(self):
        return self.title
