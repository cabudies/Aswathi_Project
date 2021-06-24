from django.db import models
from administrator.models import CustomUser

def upload_profile_pic(instance,filenname):
    return 'student_profile/{0}/of_/{1}'.format(instance.date_of_birth,filenname)

class Student(models.Model):  
    date_of_birth = models.DateField(blank=False,default="")
    profile_pic = models.FileField(upload_to=upload_profile_pic,default="")
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True) 
    semester =  models.IntegerField(default=1,blank=False)
    degree = models.ForeignKey('course.Degree',on_delete=models.CASCADE,default="")
    payment_approved = models.BooleanField(default=False,blank=True)
    student_approved = models.BooleanField(default=False,blank=True)
    academic_year = models.ForeignKey('course.AcademicYear',on_delete=models.CASCADE,default="")
    admission_id  = models.CharField(max_length=100,blank=True,default="")

    def approve(self):
        self.approved=True
        return self

    def save(self ,*args , **kwargs):
        roll_no = 1
        year = str(self.academic_year.year).replace('-',"")
        string = "000"
        self.admission_id = year+string+str(roll_no)
        roll_no+=1
        super().save(*args , **kwargs)
        

    def __str__(self):
        return self.user.first_name