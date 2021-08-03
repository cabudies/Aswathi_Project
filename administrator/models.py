from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    user_role_choices = (
        ('superadmin','Super Admin'), ('student','Student'), 
        ('teacher','Teacher'), ('hod','Head of Department'), ('hr','HR'),
        ('accountant','Accountant'),('registrar','Registrar')
    )
    gender_choices = (
        ('male', 'Male'), ('female', 'Female')
    )

    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=400, default='')
    city = models.CharField(max_length=200, default='')
    state = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')
    phone = models.IntegerField(null=True)
    email = models.EmailField(max_length=254, unique=True)
    ## passport information
    # passport_number = models.CharField(max_length=200, default='')
    # passport_issue_place = models.CharField(max_length=200, default='')
    # passport_expiry_date = models.DateTimeField(blank=True)
    # post_box_city = models.CharField(max_length=200, default='')
    # emirates_id = models.CharField(max_length=200, default='')
    # emirates_id_expiry_date = models.DateTimeField(blank=True)

    username = None
    
    role = models.CharField(max_length=50,choices=user_role_choices,default="")
    gender = models.CharField(max_length=50,choices=gender_choices,default="")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CustomUserManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.email