from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    patronymic = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.get_full_name()
