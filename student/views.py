from django.shortcuts import render
from administrator.serializers import UserSerializer 
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.response import Response
from administrator.models import CustomUser
from django.contrib.auth import get_user_model
from django.http import JsonResponse
import random , re
from rest_framework.decorators import api_view ,permission_classes, authentication_classes
from rest_framework import status
from rest_framework.generics import RetrieveAPIView , ListAPIView , CreateAPIView , UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny ,IsAuthenticated , IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema 
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Student
from .serializers import StudentObtainPairSerializer


class StudentSignupView(CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class  = UserSerializer
    queryset = CustomUser.objects.all()
    

    def create(self , request,*args , **kwargs):
        request.data._mutable = True
        request.data['role'] = 'student'
        request.data._mutable = False
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user_obj = CustomUser.objects.get(email=request.data['email'])
        student_obj = Student.objects.create(user=user_obj)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
  


class StudentLogin(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = StudentObtainPairSerializer 