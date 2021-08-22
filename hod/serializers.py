from django.db.models import fields
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from course.models import MyClass
from administrator.models import CustomUser
from rest_framework import serializers
from . import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model   
from rest_framework.response import Response


class HodObtainPairSerializer(TokenObtainPairSerializer):
   
    @classmethod
    def get_token(cls, user):
        token = super(HodObtainPairSerializer, cls).get_token(user)
        token['username'] = user.email
        return token
    
    def validate(self,attrs):
        data = super(HodObtainPairSerializer, self).validate(attrs)
        user_model = get_user_model()
        obj = user_model.objects.get(email = self.user.email)
        if obj.role == "hod":
            name = obj.first_name + obj.last_name
            data.update({'user': self.user.email})
            data.update({'role': obj.role})
            data.update({'name': name})
            return data
        else:
            msg = {'message':'You are not hod can not login'}
            return msg

class EditHodProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=CustomUser.objects.all(),
        slug_field='email')
    classes = serializers.SlugRelatedField(
        queryset=MyClass.objects.all(),
        many=True,
        slug_field='name')

    class Meta:
        model = models.HeadOfDepartment
        fields = ('user', 'classes', )

class ViewHodProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=CustomUser.objects.all(),
        slug_field='email')
    classes = serializers.SlugRelatedField(
        queryset=MyClass.objects.all(),
        many=True,
        slug_field='name')

    class Meta:
        model = models.HeadOfDepartment
        fields = ('user', 'classes')



