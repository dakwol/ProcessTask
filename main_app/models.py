from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

from main_app.enums import SERVICE_TYPES, SERVICE_STATUS_CHOICES, CLIENT_CHOICES, DIGITAL_FORMAT_CHOICES


class Organization(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название организации", blank=True, null=True, )
    code = models.CharField(max_length=50, verbose_name="Код организации", unique=True, )

    def __str__(self):
        return self.code


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=True, null=True,
    )
    patronymic = models.CharField(max_length=30, blank=True, null=True, verbose_name="Отчество")
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name="Email")
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, blank=True, null=True,
                                     verbose_name="Организация")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.get_full_name()


class LifeSituation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название жизненной ситуации", blank=True, null=True, )
    identifier = models.CharField(max_length=50, verbose_name="Идентификатор", blank=True, null=True,
                                  default="017.04.001")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь", blank=True, null=True, )

    def __str__(self):
        return self.name


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
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга",
                                blank=True, null=True, related_name='processes')
    status = models.CharField(max_length=20, choices=SERVICE_STATUS_CHOICES, default='in_queue', verbose_name="Статус",
                              blank=True, null=True)
    is_internal_client = models.BooleanField(default=False, verbose_name="Внутренний клиент", blank=True, null=True)
    is_external_client = models.BooleanField(default=False, verbose_name="Внешний клиент", blank=True, null=True)
    responsible_authority = models.CharField(max_length=255, verbose_name="Орган, ответственный за процесс", blank=True,
                                             null=True)
    department = models.CharField(max_length=255, verbose_name="Структурное подразделение органа", blank=True,
                                  null=True)
    is_digital_format = models.BooleanField(default=False, verbose_name="Цифровой формат", blank=True, null=True)
    is_non_digital_format = models.BooleanField(default=False, verbose_name="Не цифровой формат", blank=True, null=True)

    digital_format_link = models.URLField(verbose_name="Ссылка на размещение в цифровом формате", blank=True, null=True)
    identifier = models.CharField(max_length=50, verbose_name="Идентификатор", blank=True, null=True, )

    # Данные
    client_value = models.TextField(verbose_name="Ценность для клиента", blank=True, null=True)
    input_data = models.TextField(verbose_name="Данные на входе", blank=True, null=True)
    output_data = models.TextField(verbose_name="Данные на выходе", blank=True, null=True)
    related_processes = models.TextField(verbose_name="Связанные процессы", blank=True, null=True)

    def __str__(self):
        return self.identifier
