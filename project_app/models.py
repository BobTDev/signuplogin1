from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# class Signup(AbstractUser):
#     email = models.EmailField()
#     full_name = models.CharField(max_length=200)
#     username = models.CharField(max_length=200, unique=True)
#     password = models.CharField(max_length=20)
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []


class User(AbstractUser):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
