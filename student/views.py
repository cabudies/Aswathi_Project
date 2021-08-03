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
from .models import Student , StudentForm
from .serializers import StudentObtainPairSerializer , StudentDetailSerializer
from . import serializers
from rest_framework import status
from accountant.models import Payment

class StudentLogin(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = StudentObtainPairSerializer 

@api_view(['GET',])
@permission_classes([AllowAny,])
def get_details(request):
    user_id = request.query_params.get('student_id')
    student = Student.objects.get(user_id = user_id)
    payments = Payment.objects.filter(student=student,payment_method='cash')
    response_dict = {
        'cash_transactions':[]
    }
    for payment in payments:
        lst=[]
        lst.append(payment.txn_id)
        lst.append(payment.status)
        lst.append(payment.amount_paid)  
        lst.append(payment.student.admission_id)
        lst.append(payment.student.user.email)
        response_dict['cash_transactions'].append(lst)
        return Response(response_dict,status=status.HTTP_201_CREATED)

@api_view(["GET"])
@permission_classes([AllowAny,])
def student_details(request):
    admission_id = request.query_params.get('admission_id')
    try:
        student = Student.objects.get(admission_id=admission_id)
        user = CustomUser.objects.get(id = student.user_id)
        details = StudentDetailSerializer(student)
        d = dict(details.data)
        d['email'] = user.email
        d['name']  = user.first_name + user.last_name
        return Response(d,status=status.HTTP_200_OK)
    except:
       return Response({"message":"student does not exist with the gievn id"},status=status.HTTP_400_BAD_REQUEST)

class StudentForm(CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class   = serializers.StudentFormSerializer
    queryset = StudentForm.objects.all()
    
    def create(self , request,*args , **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({"message":"Okay ! we have got your data will contact you soon ",}, status=status.HTTP_201_CREATED,)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class StudentEditProfile(CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = StudentDetailSerializer
    queryset = Student.objects.all()

    def create(self , request,*args , **kwargs):
        request.data['user'] = request.user
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'message':'details updated',}, status=status.HTTP_201_CREATED,)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)