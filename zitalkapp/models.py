from django.db import models
from django.contrib.auth.models import AbstractUser

from zitalkproject import helper

class User(AbstractUser):
    """Estend functionality of user"""

    hash_id = models.CharField(max_length=32, default=helper.create_hash, unique=True)

