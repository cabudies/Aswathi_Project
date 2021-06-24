from django.contrib import admin
from teacher.models import Teacher

class TeacherModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Teacher

admin.site.register(Teacher , TeacherModelAdmin)