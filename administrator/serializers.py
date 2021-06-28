from rest_framework import serializers
from . import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model   
from rest_framework.response import Response

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
   
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.email
        return token
    
    def validate(self,attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        user_model = get_user_model()
        obj = user_model.objects.get(email = self.user.email)
        name = obj.first_name + obj.last_name
        data.update({'user': self.user.email})
        data.update({'role':obj.role})
        data.update({'name': name})
        return data


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    address = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    state = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    phone = serializers.IntegerField(required=True)
    role = serializers.CharField(required=False)  


    class Meta:
        model = models.CustomUser
        fields = ('email', 'first_name', 'password', 'last_name', 'address',
            'city', 'state', 'country', 'phone','role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



class ChangePasswordSerializers(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True,write_only=True)
    password1 = serializers.CharField(required=True,write_only=True)
    password2 = serializers.CharField(required=True,write_only=True)
  
    class Meta:
        model = models.CustomUser 
        fields = ('old_password', 'password1', 'password2')

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
        
    def validate_old_password(self , value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password1'])
        instance.save()
        return instance