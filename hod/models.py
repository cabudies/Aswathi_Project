from django.db import models
from administrator.models import CustomUser
import course.models as CourseModel

def upload_profile(instance, filename):
    return 'hod_profile/{0}/_pic/{1}'.format(instance.user.first_name,filename)

class HeadOfDepartment(models.Model):
    profile_pic = models.FileField(upload_to=upload_profile, null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    classes = models.ManyToManyField(CourseModel.MyClass)

    def __str__(self):
        return self.user.first_name