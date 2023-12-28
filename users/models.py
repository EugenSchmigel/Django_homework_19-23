from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='E-Mail')

    phone = models.CharField(max_length=35, verbose_name='Phone', **NULLABLE)
    avatar = models.ImageField(upload_to='user/', verbose_name='Avatar', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Country', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Activity')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f' {self.email}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
