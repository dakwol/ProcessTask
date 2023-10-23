from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

from main_app.enums import SERVICE_TYPES


class CustomUser(AbstractUser):
    patronymic = models.CharField(max_length=30, blank=True, null=True, verbose_name="Отчество")

    def __str__(self):
        return self.get_full_name()


class LifeSituation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название жизненной ситуации", blank=True, null=True,)
    identifier = models.CharField(max_length=50, verbose_name="Идентификатор", blank=True, null=True,)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь", blank=True, null=True,)

    def __str__(self):
        return self.identifier


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название услуги", blank=True, null=True,)
    service_type = models.CharField(max_length=10, choices=SERVICE_TYPES, verbose_name="Тип услуги", blank=True,
                                    null=True,)
    regulating_act = models.CharField(max_length=255, verbose_name="Регулирующий акт", blank=True, null=True,)
    lifesituation = models.ForeignKey(LifeSituation, on_delete=models.CASCADE, verbose_name="Жизненная ситуация",
                                      blank=True, null=True, related_name='services')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь", blank=True, null=True, )

    def __str__(self):
        return self.name
