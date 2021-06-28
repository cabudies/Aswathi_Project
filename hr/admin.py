from django.contrib import admin
from .models import Hr
class HrModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Hr
        list_display = ('profile_pic','name')

        def get_name(self,obj):
            return self.user.first_name
        get_name.short_description = "Name"

admin.site.register(Hr , HrModelAdmin)