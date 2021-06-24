from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin
from . import resource

class CustomerUserAdmin(ImportExportModelAdmin, UserAdmin):
    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return False
    
    class Meta:
        model = models.CustomUser

    resource_class = resource.ImportUserResource 
    list_display = ('id','email', 'first_name', 'city','state','role')
    search_fields = ('email', 'first_name', 'city')
    list_filter = ('city', 'state', 'country')
    ordering = ('-created_at',)  
    fieldsets = (
        (
            'User Details', 
            {
                'fields': ('email', 'first_name', 'last_name', 
                    'phone', 'address', 'city', 'state', 'country', 'password','role')
            }
        ),
    )

    def get_export_resource_class(self):
        return resource.ExportUserResource

admin.site.register(models.CustomUser, CustomerUserAdmin)