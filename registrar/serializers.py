from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model


class RegistrarObtainPairSerializer(TokenObtainPairSerializer):
   
    @classmethod
    def get_token(cls, user):
        token = super(RegistrarObtainPairSerializer, cls).get_token(user)
        token['username'] = user.email
        return token
    
    def validate(self,attrs):
        data = super(RegistrarObtainPairSerializer, self).validate(attrs)
        user_model = get_user_model()
        obj = user_model.objects.get(email = self.user.email)
        name = obj.first_name + obj.last_name
        if obj.role == 'registrar':
            data.update({'user': self.user.email})
            data.update({'role': obj.role})
            data.update({'name': name})
            return data
        else:
            msg = {'message': "You are not Registrar"}
            return msg