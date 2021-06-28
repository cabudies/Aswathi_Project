from django.contrib import admin
from teacher.models import Teacher

class TeacherModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Teacher
        list_display = ('profile_pic','name')

        def get_name(self,obj):
            return self.user.first_name
        get_name.short_description = "Name"

admin.site.register(Teacher , TeacherModelAdmin)