from django.db import models
from administrator.models import CustomUser

def return_hr_image(instance,filename):
    return 'hr/{0}/profile_pic/{1}'.format(instance.user.email,filename)


class Hr(models.Model):
    profile_pic = models.FileField(upload_to=return_hr_image)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

