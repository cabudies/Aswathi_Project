from django.contrib import admin
from . import models


class PayementModelAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Payment
    list_display = ('txn_id','status','payment_method','status','student')

admin.site.register(models.Payment,PayementModelAdmin)


class AccountantModelAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Payment
        list_display = ('profile_pic','name')

        def get_name(self,obj):
            return self.user.first_name
        get_name.short_description = "Name"
        

admin.site.register(models.Accountant,AccountantModelAdmin)