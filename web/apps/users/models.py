import uuid

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser, PermissionsMixin):
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False, db_index=True)
    email = models.EmailField(null=True, blank=True)
    username = models.CharField(max_length=150, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'uuid'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def __repr__(self):
        return f'<CustomUser uuid={self.uuid} username={self.username}>'
