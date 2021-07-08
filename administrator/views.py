
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.response import Response
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.http import JsonResponse
import random , re
from rest_framework.decorators import api_view ,permission_classes, authentication_classes
from . import serializers
from rest_framework import status
from rest_framework.generics import RetrieveAPIView , ListAPIView , CreateAPIView , UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny ,IsAuthenticated , IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer, UserSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema 
from rest_framework_simplejwt.tokens import RefreshToken
from aswathi.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from .models import CustomUser
from student.models import Student

class LoginTokenView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer 
    
@swagger_auto_schema(methods=['POST',], request_body=serializers.UserSerializer)
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny,])
def createuser(request):
    serializer = serializers.UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors,status=status.HTTP_205_RESET_CONTENT)




class LogoutView(APIView):
    permission_classes=[AllowAny,]

    def post(self,request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message":"You successfully logged out"})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

class ChangePasswordView(UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class  = serializers.ChangePasswordSerializers
    queryset = CustomUser.objects.all()


@api_view(["POST",])
@permission_classes([IsAuthenticated,])
def approve(request):
    stu_id = request.data.get('admission_id')
    print(stu_id.strip())
    student = Student.objects.get(admission_id=stu_id.strip())
    if stu_id is not None:
        try:
            student = Student.objects.get(admission_id=stu_id)
        # user = CustomUser.objects.get(id=student_id)
            student.student_approved = True
            student.save()
            print(student.student_approved)
        # subject = "Login Credentials"
        # message = 'Hello Your Login credentials your email'+user.email+"and your password is " + user.password
        # recepient = str(user.email)
        # send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            return Response({'message':"Student got approved and login credentials has been sent"},status=status.HTTP_202_ACCEPTED)
        except Student.DoesNotExist:
            return Response({"message":"student does not exists"},status=status.HTTP_400_BAD_REQUEST)

class StudentSignupView(CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class  = UserSerializer
    queryset = CustomUser.objects.all()
       

    def create(self , request,*args , **kwargs):
       
        request.data['role'] = 'student'
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user_obj = CustomUser.objects.get(email=request.data['email'])
        student_obj = Student.objects.create(user=user_obj)
        headers = self.get_success_headers(serializer.data)
        return Response({"message":"Student has been registered",'data':serializer.data}, status=status.HTTP_201_CREATED, headers=headers)