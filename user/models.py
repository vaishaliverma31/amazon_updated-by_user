from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_amazon_admin = models.BooleanField(default=False)
    is_amazon_employee = models.BooleanField(default=False)
    is_amazon_customer = models.BooleanField(default=True)


