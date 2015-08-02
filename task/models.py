from django.db import models
from django.contrib.auth.models import User, AbstractUser


"""
A Simple Wrapper for Auth User. So Every Db query get run run in models
"""


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=150)

    @classmethod
    def create_user(cls, **kwargs):
        user = cls.objects.create(**kwargs)
        return user

    @classmethod
    def filter_user(cls, **kwargs):
        user = cls.objects.filter(**kwargs)
        return user

    @classmethod
    def get_user(cls, **kwargs):
        user = cls.objects.get(**kwargs)
        return user
