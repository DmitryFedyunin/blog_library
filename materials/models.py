from django.db import models

class Materials(models.Model):
    title = models.CharField('Название', max_length=100)
    author = models.CharField('Автор',max_length= 150)
    type = models.CharField('Тип', max_length=50)
    category = models.CharField('Категория', max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
    #функция для созвращения на страницу после обновение записи
    def get_absolute_url(self):
        return f'/'

    class Meta:
        verbose_name = 'Материалы'
        verbose_name_plural= 'Материалы'