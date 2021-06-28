from django.contrib import admin
from .models import HeadOfDepartment

class HodModelAdmin(admin.ModelAdmin):
    class Meta:
        model = HeadOfDepartment

admin.site.register(HeadOfDepartment,HodModelAdmin)