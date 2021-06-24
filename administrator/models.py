from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=400, default='')
    city = models.CharField(max_length=200, default='')
    state = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')
    phone = models.IntegerField(null=True)
    email = models.EmailField(max_length=254, unique=True)
    username = None
    choices = (
        ('superadmin','superadmin'),('student','student'),('teacher','teacher')
        ,('hod','hod'),('hr','hr'),('accountant','accountant'),('registrar','registrar')    )
    role = models.CharField(max_length=50,choices=choices,default="")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CustomUserManager()

   

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.email