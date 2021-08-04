from django.contrib import admin
from .models import Student , StudentForm


class StudentModelAdmin(admin.ModelAdmin):

    class Meta:
        model = Student
    list_display = ('admission_id','date_of_birth','get_email','get_name')

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'  
    get_email.admin_order_field = 'user__email'

    def get_name(self, obj):
        return obj.user.first_name + " "  + obj.user.last_name
    get_email.short_description = 'Name'  
    get_email.admin_order_field = 'user__email'

class StudentFormAdmin(admin.ModelAdmin):

    class Meta:
        model = StudentForm
    list_display = ('name','email','phone','course_interested')

admin.site.register(Student,StudentModelAdmin) 
admin.site.register(StudentForm,StudentFormAdmin)     