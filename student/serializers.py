from rest_framework import serializers
from . import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model   
from rest_framework.response import Response
from student.models import Student



class StudentObtainPairSerializer(TokenObtainPairSerializer):
   
    @classmethod
    def get_token(cls, user):
        token = super(StudentObtainPairSerializer, cls).get_token(user)
        token['username'] = user.email
        return token
    
    def validate(self,attrs):
        data = super(StudentObtainPairSerializer, self).validate(attrs)
        user_model = get_user_model()
        obj = user_model.objects.get(email = self.user.email)
        try:
            student = Student.objects.get(user_id=obj.id)
            if student.student_approved == True:
                name = obj.first_name + obj.last_name
                data.update({'user': self.user.email})
                data.update({'role': obj.role})
                data.update({'name': name})
                return data
            else:
                data={'Message':'You can not login , please contact registrar.'}
                return data
        except Student.DoesNotExist:
            msg = {"message":"You are not an Student"}
            return msg
