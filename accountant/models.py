from administrator.models import CustomUser
from django.db import models
from django.utils import translation
import uuid
import random
from student import models as stumodels
from course.models import Degree
class Payment(models.Model):
    methods = (
        ('Online','Online'),
        ('cash','Offline'),
    )
    payment_method = models.CharField(choices=methods,max_length=10)
    amount_paid = models.FloatField(default=None,blank=True)
    trn_id  = uuid.uuid4()
    txn_id = models.CharField(max_length=100,default=trn_id,blank=False)
    l = ["pending","success"]
    status = random.choice(l)
    status = models.CharField(default=status,blank=False,max_length=10)
    done_at = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(stumodels.Student,on_delete=models.CASCADE,default="")
    course = models.ForeignKey(Degree,on_delete=models.CASCADE,default="")

    def __str__(self):
        return self.txn_id
    

def upload_profile_pic(instance,filename):
    return 'accountant_profile/{0}/_pic/{1}'.format(instance.user.first_name,filename)

class Accountant(models.Model):
    profile_pic = models.FileField(upload_to=upload_profile_pic)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return self.user.first_name