from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    patronymic = models.CharField(max_length=30, blank=True, null=True, verbose_name="Отчество")

    def __str__(self):
        return self.get_full_name()


class LifeSituation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название жизненной ситуации")
    identifier = models.CharField(max_length=50, verbose_name="Идентификатор")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return self.identifier
