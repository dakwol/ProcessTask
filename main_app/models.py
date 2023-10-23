from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

from main_app.enums import SERVICE_TYPES, SERVICE_STATUS_CHOICES, CLIENT_CHOICES, DIGITAL_FORMAT_CHOICES


class CustomUser(AbstractUser):
    patronymic = models.CharField(max_length=30, blank=True, null=True, verbose_name="Отчество")

    def __str__(self):
        return self.get_full_name()


class LifeSituation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название жизненной ситуации", blank=True, null=True, )
    identifier = models.CharField(max_length=50, verbose_name="Идентификатор", blank=True, null=True, )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь", blank=True, null=True, )

    def __str__(self):
        return self.identifier


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название услуги", blank=True, null=True, )
    service_type = models.CharField(max_length=10, choices=SERVICE_TYPES, verbose_name="Тип услуги", blank=True,
                                    null=True, )
    regulating_act = models.CharField(max_length=255, verbose_name="Регулирующий акт", blank=True, null=True, )
    lifesituation = models.ForeignKey(LifeSituation, on_delete=models.CASCADE, verbose_name="Жизненная ситуация",
                                      blank=True, null=True, related_name='services')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь", blank=True, null=True, )

    def __str__(self):
        return self.name


class Process(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название процесса", blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга, на которую ссылается",
                                blank=True, null=True, related_name='processes')
    status = models.CharField(max_length=20, choices=SERVICE_STATUS_CHOICES, default='in_queue', verbose_name="Статус")
    client = models.CharField(max_length=20, choices=CLIENT_CHOICES, verbose_name="Клиент")
    responsible_authority = models.CharField(max_length=255, verbose_name="Орган, ответственный за процесс", blank=True,
                                             null=True)
    department = models.CharField(max_length=255, verbose_name="Структурное подразделение органа", blank=True,
                                  null=True)
    digital_format = models.CharField(
        max_length=20,
        choices=DIGITAL_FORMAT_CHOICES,
        default='digital',
        verbose_name="Цифровой формат",
        blank=True, null=True
    )
    digital_format_link = models.URLField(verbose_name="Ссылка на размещение в цифровом формате", blank=True, null=True)
    identifier = models.CharField(max_length=50, verbose_name="Идентификатор", blank=True, null=True, )

    def __str__(self):
        return self.name
