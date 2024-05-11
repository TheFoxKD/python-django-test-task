import uuid

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser, PermissionsMixin):
    """
    Attributes:
        uuid: The UUID of the user. Primary key.
        username: The username of the user. From AbstractUser.
        date_joined: The date the user joined. From AbstractUser.
        is_active: Whether the user is active. From AbstractUser.

    """
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False, db_index=True)
    email = models.EmailField(verbose_name=_('email address'), unique=True)

    USERNAME_FIELD = 'uuid'
    REQUIRED_FIELDS = ['username', 'email']

    def __str__(self):
        return self.username

    def __repr__(self):
        return f'<CustomUser uuid={self.uuid} username={self.username}>'
