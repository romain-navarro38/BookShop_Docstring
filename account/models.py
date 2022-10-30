from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("L'adresse email est obligatoire.")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs["is_staff"] = True
        kwargs["is_superuser"] = True
        kwargs["is_active"] = True

        return self.create_user(email=email, password=password, **kwargs)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=200, blank=True, verbose_name='Pseudo')
    email = models.EmailField(max_length=200, unique=True)
    stripe_id = models.CharField(max_length=100, blank=True, verbose_name='ID Stripe')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = "Utilisateur"

    def __str__(self):
        return self.username or self.get_full_name() or self.email

    def save(self, *args, **kwargs):
        if self.first_name:
            self.first_name = self.first_name.title()
        if self.last_name:
            self.last_name = self.last_name.title()
        super().save(*args, **kwargs)
