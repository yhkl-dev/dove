from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField("name", max_length=32, null=True, help_text="name")
    phone_number = models.CharField("phone number", max_length=11, null=True, help_text="phone number")
    id_rsa_key = models.TextField(null=True)
    id_rsa_pub = models.TextField(null=True)

    class Meta:
        verbose_name = "website user"
        ordering = ["id"]
        db_table = "auth_user"
        permissions = (
            ("can_view_user", "can view user")
        )

    def __str__(self):
        return self.username
