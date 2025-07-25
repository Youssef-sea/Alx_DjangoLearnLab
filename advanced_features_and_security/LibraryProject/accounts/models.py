# advanced_features_and_security/accounts/models.py
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    # Remove the default 'username' field if you want to use email for authentication
    # You might want to keep it if you still want a distinct username.
    # For this example, we'll assume email is the primary identifier.
    username = None # Set username to None to remove it from AbstractUser

    email = models.EmailField(unique=True, null=False, blank=False)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    # Specify that email is used as the unique identifier for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # No extra required fields beyond email for superuser creation

    def __str__(self):
        return self.email