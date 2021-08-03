from django.db import models
from administrator.models import CustomUser

def upload_profile_pic(instance,filenname):
    return 'student_profile/{0}/of_/{1}'.format(instance.date_of_birth,filenname)

class Student(models.Model):
    academic_season_choices = (
        ('fall', 'Fall'), ('spring', 'Spring'),
        ('summer_i', 'Summer I'), ('summer_ii', 'Summer II')
    )
    study_mode_choices = (
        ('day', 'Day'), ('evening', 'Evening'),
        ('weekend', 'Weekend')
    )
    apply_as_choices = (
        ('freshman', 'Fresh man'), ('transfer', 'Transfer'),
        ('foundation', 'Foundation'), ('returning', 'Returning'),
        ('visiting', 'Visiting')
    )
    emergency_contact_relation_choices = (
        ('father', 'Father'), ('mother', 'Mother'),
        ('son', 'Son'), ('daughter', 'Daugther'),
        ('brother', 'Brother'), ('sister', 'Sister'),
        ('husband', 'Husband'), ('wife', 'Wife'),
        ('uncle', 'Uncle'), ('aunt', 'Aunt'),
    )
    high_school_certificate_choices = (
        ('general_secondary', 'General Secondary Certificate'),
        ('high_school_diploma', 'High School Diploma'),
        ('british_certificate', 'British Certificate'),
        ('ib', 'IB')
    )
    english_language_test_name_choices = (
        ('tofel', 'TOFEL'), ('ielts', 'IELTS'),
    )
    documentation_checklist_choices = (
        ('submitted', 'Submitted'), ('missing', 'Missing'),
        ('not_applicable', 'Not Applicable')
    )

    profile_pic = models.FileField(upload_to=upload_profile_pic,default="",blank=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True) 
    semester = models.IntegerField(default=1,blank=True)
    degree = models.ForeignKey('course.Degree',on_delete=models.CASCADE,default="",null=True,blank=True)
    payment_approved = models.BooleanField(default=False,blank=True)
    student_approved = models.BooleanField(default=False,blank=True)
    academic_year = models.CharField(max_length=10,default="2020-21",blank=True)
    admission_id  = models.CharField(max_length=100,blank=True,default="")
    ## personal information
    date_of_birth = models.DateField(blank=True, default="1999-07-09")
    birth_place = models.CharField(max_length=255, blank=True, verbose_name='Name of the city where you were born')
    ## passport information
    passport_number = models.CharField(max_length=200, default='')
    passport_issue_place = models.CharField(max_length=200, default='')
    passport_expiry_date = models.DateTimeField(blank=True)
    post_box_city = models.CharField(max_length=200, default='')
    emirates_id = models.CharField(max_length=200, default='')
    emirates_id_expiry_date = models.DateTimeField(blank=True)
    ## application information
    academic_season = models.CharField(max_length=50, choices=academic_season_choices, default="")
    study_mode = models.CharField(max_length=50, choices=study_mode_choices, default="")
    apply_as = models.CharField(max_length=50, choices=apply_as_choices, default="")
    ## emergency information
    emergency_contact_first_name = models.CharField(max_length=255, default='')
    emergency_contact_last_name = models.CharField(max_length=255, default='')
    emergency_contact_city = models.CharField(max_length=255, default='')
    emergency_contact_country = models.CharField(max_length=255, default='')
    emergency_contact_mobile = models.PositiveIntegerField(blank=True)
    emergency_contact_telephone_number = models.PositiveIntegerField(blank=True)
    emergency_contact_email = models.EmailField(max_length=255, unique=True)
    emergency_contact_relationship = models.CharField(max_length=100, choices=emergency_contact_relation_choices, default="")
    ## education information
    high_school_name = models.CharField(max_length=255, default='')
    high_school_city = models.CharField(max_length=255, default='')
    high_school_country = models.CharField(max_length=255, default='')
    high_school_academic_year = models.PositiveIntegerField(default=0)
    high_school_percentage = models.DecimalField(blank=True)
    high_school_certificate_type = models.CharField(max_length=100, choices=high_school_certificate_choices, default="")
    ## transfer student information
    transfer_college_name = models.CharField(max_length=255, default='')
    transfer_college_city = models.CharField(max_length=255, default='')
    transfer_college_country = models.CharField(max_length=255, default='')
    transfer_college_academic_year = models.PositiveIntegerField(default=0)
    transfer_college_percentage = models.DecimalField(blank=True)
    ## english profienciey
    english_language_test_name = models.CharField(max_length=100, choices=english_language_test_name_choices, default="")
    english_language_test_score = models.DecimalField(blank=True)
    english_language_test_date = models.DateField(blank=True)
    ## documentation checklist
    application_form_completed = models.CharField(max_length=100, choices=documentation_checklist_choices, default="")
    high_school_certificate = models.CharField(max_length=100, choices=documentation_checklist_choices, default="")
    transfer_college_certificate = models.CharField(max_length=100, choices=documentation_checklist_choices, default="")
    english_language_test_score_card = models.CharField(max_length=100, choices=documentation_checklist_choices, default="")
    passport_size_photos = models.CharField(max_length=100, choices=documentation_checklist_choices, default="")
    uae_residency_visa = models.CharField(max_length=100, choices=documentation_checklist_choices, default="")
    national_card = models.CharField(max_length=100, choices=documentation_checklist_choices, default="")
    application_fee = models.CharField(max_length=100, choices=documentation_checklist_choices, default="")
    medical_insurance = models.CharField(max_length=100, choices=documentation_checklist_choices, default="")

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

class StudentForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70,unique=True)
    phone = models.IntegerField(unique=True)
    course_interested  = models.CharField(max_length=60)

    def __str__(self):
        return self.name