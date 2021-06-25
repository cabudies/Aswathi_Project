from django.db import models
from administrator.models import CustomUser

# registrar directory
def upload_profile(instance, filename):
    return 'registrar_profile/{0}/_pic/{1}'.format(instance.user.first_name,filename)

class Registrar(models.Model):
    profile_pic = models.FileField(upload_to=upload_profile)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return self.user.first_name