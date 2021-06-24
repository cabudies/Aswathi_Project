from import_export import resources, fields
from .models import CustomUser

class ImportUserResource(resources.ModelResource):
    password = fields.Field(attribute='password', column_name='password')

    def before_save_instance(self, instance, using_transactions, dry_run):
        instance.set_password(getattr(instance, 'password'))

    class Meta:
        model = CustomUser
        import_id_fields = ('email',)
        fields = (
            'email', 'password', 'first_name', 'last_name', 'phone',
            'address', 'city', 'state', 'country', 'role',
            )
            
class ExportUserResource(resources.ModelResource):
    
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone',
            'address', 'city', 'state', 'country',)
        export_order = ('email', 'first_name', 'last_name', 'phone',
            'address', 'city', 'state', 'country')

