from django.db import models
from student.models import Student

class Subjects(models.Model):
    name = models.CharField(max_length=50, default="", blank=False)
    credit = models.IntegerField(default=0)
    teacher = models.ForeignKey('teacher.Teacher',on_delete=models.CASCADE,default="")

    def __str__(self) -> str:
        return self.name
    
class Degree(models.Model):
    name = models.CharField(max_length=255, default="", blank=False)
    duration = models.IntegerField(default=1,blank=False)
    total_semesters = models.IntegerField(default="")
    
    def __str__(self):
        return self.name



class MyClass(models.Model):
    name = models.CharField(max_length=100,default="")
    Subjects = models.ManyToManyField(Subjects)
    is_class_live = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

def get_material_dir(instance):
    return 'class/{0}/booklet/{1}/'.format(instance.file_class.name,filename)


def get_material_notes_dir(instance):
    return 'class/{0}/notes/{1}/'.format(instance.file_class.name,filename)


class Material(models.Model):
    booklet = models.FileField(upload_to=get_material_dir)
    notes =  models.FileField(upload_to=get_material_notes_dir)
    file_class = models.ForeignKey(MyClass, on_delete=models.CASCADE)

class Fee(models.Model):
    fee_name = models.CharField(
        max_length=50,
        default='tuition_fee')
    amount   = models.IntegerField()
    course   = models.ForeignKey(
        Degree, 
        on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.fee_name