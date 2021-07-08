from django.shortcuts import render
from . import serializers
from aswathi.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny ,IsAuthenticated , IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from student.models import Student
from rest_framework.decorators import api_view , permission_classes
from rest_framework import status
from accountant.models import Payment
from rest_framework.pagination import PageNumberPagination
from administrator.models import CustomUser

class RegistrarLoginView(TokenObtainPairView):
    permission_classes  = [AllowAny,]
    serializer_class = serializers.RegistrarObtainPairSerializer


@api_view(["GET",])
@permission_classes([IsAuthenticated,])
def approve_student(request):

    pk = request.query_params.get('student_id',None)
    student = Student.objects.get(user_id=pk)
    user = CustomUser.objects.get(id=pk)
    if student.payment_approved == True:
       student.student_approved = True
       student_mail = student.user.email
       student_name = student.user.first_name  
       #subject = "Login Credentials"
       #message = "Hello Your Login credentials your email"
       #recepient = str(user.email)
       #send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
       data = {'message':'Student Approved','student name':student_name}
       return Response(data)
    else:
        data = {'message':"student's payment is due."}
        return Response(data,status=status.HTTP_201_CREATED)




@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def cash_payments(request):
    

    student_id = request.query_params.get('student_id',None)
    if student_id is None:
        paginator = PageNumberPagination()
        paginator.page_size = 10
        response_dict = { 
                'cash_transactions':[],

            }
        
        payments = Payment.objects.all()
        for payment in payments:

            dct = { 'txn_id':1,
                    'amount paid':3,
                    'admission_id':8,
                    'email':8,
                  }

            dct['txn_id']=(payment.txn_id)
            dct['amount_paid']=(payment.amount_paid)
            dct['admission_id']=payment.student.admission_id
            dct['email']=(payment.student.user.email)
            dct['student degreee'] = payment.student.degree.name
            dct['payment_approved']=(payment.student.payment_approved)
            response_dict['cash_transactions'].append(dct)
        return Response(response_dict,status=status.HTTP_202_ACCEPTED)
    elif student_id is not None:
        paginator = PageNumberPagination()
        paginator.page_size = 10
        response_dict = { 
                'cash_transactions':[],}
        
        payments = Payment.objects.filter(student__user_id=student_id)
        for payment in payments:

            dct = { 'txn_id':1,
                    'amount paid':3,
                    'admission_id':8,
                    'email':8,
                  }

            dct['txn_id']=(payment.txn_id)
            dct['amount_paid']=(payment.amount_paid)
            dct['admission_id']=payment.student.admission_id
            dct['email']=(payment.student.user.email)
            response_dict['cash_transactions'].append(dct)
        return Response(response_dict,status=status.HTTP_202_ACCEPTED)


    else:

        return Response({

           "Message":"Not a valid query."

        },status=staus.HTTP_400_BAD_REQUEST)