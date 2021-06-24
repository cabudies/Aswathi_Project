from django.contrib import admin
from . import models

class MyClassModelAdmin(admin.ModelAdmin):
    class Meta:
        model = models.MyClass
        list_display = '__all__'

class DegreeModelAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Degree

admin.site.register(models.MyClass , MyClassModelAdmin)
admin.site.register(models.Degree,DegreeModelAdmin)
admin.site.register(models.Subjects)
admin.site.register(models.Material)
admin.site.register(models.AcademicYear)