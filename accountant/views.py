from django.shortcuts import render
from . import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny ,IsAuthenticated , IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Payment
from rest_framework.decorators import api_view , permission_classes
from rest_framework import status
from student.models import Student
from rest_framework.pagination import PageNumberPagination

class AccountantLoginView(TokenObtainPairView):
    permission_classes  = [AllowAny,]
    serializer_class = serializers.AccountantObtainPairSerializer


@api_view(["GET",])
@permission_classes([AllowAny,])
def approve_payment(request):
    pk = request.query_params.get('pk',None)
    try:
        student = Student.objects.get(user_id=pk)
        payment = Payment.objects.get(student=student)
        if payment.status == "success":
            student.payment_approved == True   
            data = {'Message': "Payment Approved",
                    'student': student.user.email}
            return Response(data,status=status.HTTP_200_OK)
        else:
           return Response({"message":"Your payment was not successfull"})
    except Student.DoesNotExist:
        return Response({"message":"student with this id does not exist"},status=status.HTTP_400_BAD_REQUEST)


  

@api_view(['GET'])
@permission_classes([AllowAny,])
def cash_payments(request):
    
    status_ = request.query_params.get('status_',None)
    if status_ is None:
        paginator = PageNumberPagination()
        paginator.page_size = 10
        response_dict = {
            'txn_ids':[],
            'status':[],
            'amount':[],
            'admission_ids':[],
            'emails':[],
        }
        payments = Payment.objects.all()
        for payment in payments:
            response_dict['txn_ids'].append(payment.txn_id)
            response_dict['status'].append(payment.status)
            response_dict['amount'].append(payment.amount_paid)
            response_dict['admission_ids'].append(payment.student.admission_id)
            response_dict['emails'].append(payment.student.user.email)
        return Response(response_dict,status= status.HTTP_200_OK)
    elif status_=="success":
        paginator = PageNumberPagination()
        paginator.page_size = 10
        response_dict = {
            'txn_ids':[],
            'status':[],
            'amount':[],
            'admission_ids':[],
            'emails':[],
        }
        payments = Payment.objects.filter(status="success")
        for payment in payments:
            response_dict['txn_ids'].append(payment.txn_id)
            response_dict['status'].append(payment.status)
            response_dict['amount'].append(payment.amount_paid)
            response_dict['admission_ids'].append(payment.student.admission_id)
            response_dict['emails'].append(payment.student.user.email)
        return Response(response_dict,status= status.HTTP_200_OK)
    elif status_ == "pending":
        paginator = PageNumberPagination()
        paginator.page_size = 10
        response_dict = {
            'txn_ids':[],
            'status':[],
            'amount':[],
            'admission_ids':[],
            'emails':[],
        }
        payments = Payment.objects.filter(status="pending")
        for payment in payments:
            response_dict['txn_ids'].append(payment.txn_id)
            response_dict['status'].append(payment.status)
            response_dict['amount'].append(payment.amount_paid)
            response_dict['admission_ids'].append(payment.student.admission_id)
            response_dict['emails'].append(payment.student.user.email)
        return Response(response_dict,status= status.HTTP_200_OK)
    else:
        return Response({
           "Message":"Not a valid query."
        })

@api_view(["GET",])
@permission_classes([AllowAny,])
def get_payment_details(request):
    pk = request.query_params.get('pk',None)
    if pk is not None:
        student = Student.objects.get(user_id=pk)
        payments = Payment.objects.filter(student=student)
        data = {'name_of_student':student.user.first_name,
                'course':[],
                'payment_method':[],
                'txn_id':[]}
        for i in payments:
            data['course'].append(i.course.name)
            data['payment_method'].append(i.payment_method)
            data['txn_id'].append(i.txn_id)
        return Response(data,status=status.HTTP_200_OK)
    else:
        return Response({"message":"Please mention the student's ID"},status=status.HTTP_400_BAD_REQUEST)
