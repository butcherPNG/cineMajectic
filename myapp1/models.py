from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    username = models.CharField(verbose_name='login', max_length=254, blank=False, unique=True)
    phone_number = models.CharField(verbose_name='phone_number', max_length=254, blank=False, unique=True)
    email = models.CharField(verbose_name='email', max_length=254, blank=False, unique=True)
    password = models.CharField(verbose_name='password', max_length=254, blank=False)

    # username = models.CharField(verbose_name='login', max_length=254, blank=False, unique=True)
    # name = models.CharField(verbose_name='name', max_length=254, blank=False)
    # surname = models.CharField(verbose_name='surname', max_length=254, blank=False)
    # patronymic = models.CharField(verbose_name='patromymic', max_length=254, blank=True)
    # password = models.CharField(verbose_name='password', max_length=254, blank=False)
    # email = models.CharField(verbose_name='email', max_length=254, blank=False, unique=True)


    USERNAME_FIELD = 'username'


    def __str__(self):
        return self.username



class SearchQuery(models.Model):
    query_text = models.CharField(max_length=255, default='Введите адрес')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query_text