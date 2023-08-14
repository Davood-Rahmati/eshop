from django.db import models

from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11, unique=True)
    date_of_birth = models.DateTimeField()
    national_code = models.IntegerField()
    email = models.EmailField(max_length=255, unique=True)
    sheba_bank = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    address_3 = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['email']
    is_admin = models.BooleanField(default=False)


    def __str__(self):
        return True

    def has_perm(self, perm, obj=None):
        return True

    @property
    def is_staff(self):
        return self.is_admin

