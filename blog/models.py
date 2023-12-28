from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, **NULLABLE, verbose_name='slug')
    content = models.TextField(**NULLABLE, verbose_name='содержимое')
    photo = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='превью')
    create_date = models.DateTimeField(**NULLABLE, verbose_name='дата создания')
    update_date = models.DateTimeField(**NULLABLE, verbose_name='признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')
    is_published = models.BooleanField(default=True, verbose_name='Published')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
