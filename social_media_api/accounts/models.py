from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    # Users this user is following
    following = models.ManyToManyField(
        'self',
        symmetrical=False,    # One-way relationship
        related_name='followers',  # Reverse lookup: who follows this user
        blank=True
    )

    def __str__(self):
        return self.username
