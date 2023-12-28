from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    photo = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')

    price = models.IntegerField(**NULLABLE, verbose_name='цена за покупку')
    create_date = models.DateTimeField(**NULLABLE, verbose_name='дата создания')
    update_date = models.DateTimeField(**NULLABLE, verbose_name='дата последнего изменения')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

        permissions = [
            (
                'set_is_published',
                'Can publish post'
            ),
            (
                'set_description',
                'Can change description'
            ),
            (
                'set_category',
                'Can change category'
            )
        ]


class Version(models.Model):
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=50, verbose_name='Название версии')
    is_active = models.BooleanField(default=True, verbose_name='Признак текущей версии')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')

    def __str__(self):
        return f'{self.version_number}, {self.version_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'


