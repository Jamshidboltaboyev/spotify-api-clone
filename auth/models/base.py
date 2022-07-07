from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    pass


class User(AbstractBaseUser):
    class Genders(models.TextChoices):
        male = 'm', 'Male'
        female = 'f', 'Female'
        none = 'n', 'Non-binary'

    objects = CustomUserManager()

    display_name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=Genders.choices)
