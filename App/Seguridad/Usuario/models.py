from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    PAIS_CHOICES = (
        (1, 'Nicaragua'),
        (2, 'Honduras'),
        (3, 'Costa Rica'),
        (4, 'Panamá'),
    )

    pais = models.IntegerField(choices=PAIS_CHOICES, default=1)

    def __str__(self):
        return f"{self.username} ({self.get_pais_display()})"


