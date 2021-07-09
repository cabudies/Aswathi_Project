from django.db import models
from administrator.models import CustomUser

def upload_profile_pic(instance,filenname):
    return 'student_profile/{0}/of_/{1}'.format(instance.date_of_birth,filenname)

class Student(models.Model):  
    date_of_birth = models.DateField(blank=True,default="1999-07-09")
    profile_pic = models.FileField(upload_to=upload_profile_pic,default="",blank=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True) 
    semester =  models.IntegerField(default=1,blank=True)
    degree = models.ForeignKey('course.Degree',on_delete=models.CASCADE,default="",null=True,blank=True)
    payment_approved = models.BooleanField(default=False,blank=True)
    student_approved = models.BooleanField(default=False,blank=True)
    academic_year = models.CharField(max_length=10,default="2020-21",blank=True)
    admission_id  = models.CharField(max_length=100,blank=True,default="")

    def approve(self):
        self.student_approved=True
        return self
  
    def save(self ,*args , **kwargs):
        
        year_ = str(self.academic_year).replace("-", "")
        string = "0"
        self.admission_id = year_+string+(str(self.date_of_birth).replace('-',"")[4:])
        super().save(*args , **kwargs)
        

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name