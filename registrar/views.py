from django.shortcuts import render
from . import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny ,IsAuthenticated , IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from student.models import Student
from rest_framework.decorators import api_view , permission_classes
from rest_framework import status


class RegistrarLoginView(TokenObtainPairView):
    permission_classes  = [AllowAny,]
    serializer_class = serializers.RegistrarObtainPairSerializer

@api_view(["GET",])
@permission_classes([AllowAny,])
def approve_student(request):
    pk = request.query_params.get('pk',None)
    student = Student.objects.get(user_id=pk)
    if student.payment_approved == True:
       student.student_approved = True
       student_mail = student.user.email
       student_name = student.user.first_name  
       data = {'message':'Student Approved',
               'student name':student_name,
               'student_mail':student_mail}
       return Response(data,status=status.HTTP_200_OK)
    else:
        data = {'message':"student's payment is due."}
        return Response(data)