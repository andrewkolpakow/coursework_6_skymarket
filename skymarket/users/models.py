from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from django.db.models import TextChoices

from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles(TextChoices):
    # TODO закончите enum-класс для пользователя
    USER = "user", "Пользователь"
    ADMIN = "admin", "Админ"


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.USER)
    image = models.ImageField(upload_to="ad_image", blank=True, null=True)

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin