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
from course.models import Fee

class AccountantLoginView(TokenObtainPairView):
    permission_classes  = [AllowAny,]
    serializer_class = serializers.AccountantObtainPairSerializer



@api_view(["GET","POST"])
@permission_classes([AllowAny,])
def approve_payment(request):

    pk = request.data.get('admission_id')
    print(pk)
    try:
        student = Student.objects.get(admission_id=pk)
        payment = Payment.objects.get(student=student)
        if payment.status == "success":
            student.payment_approved == True   
            data = {'message': "Payment Approved",'email': student.user.email}
            return Response(data)
        else:
            return Response({"message":"Your payment was not successfull"})
    except Student.DoesNotExist:
        return Response({"message":"student with this id does not exist"},status=status.HTTP_400_BAD_REQUEST)



import random
@api_view(["POST"])
@permission_classes([IsAuthenticated,])
def add_cash(request):
    number = str(random.randint(100, 500))  
    number2 = str(random.randrange(898))
    invoice_id = number+number2
    stu_id = request.data.get('addmission_id')
    amount =  request.data.get('payment')
    fee_type= request.data.get('fee_type')
    course = request.data.get('degree')
    if stu_id is None:
        return Response({"message":"Please enter which student's cash you want to add"},status=status.HTTP_400_BAD_REQUEST)
    if amount is None:
        return Response({"message":"Please enterramount to add"},status=status.HTTP_400_BAD_REQUEST)
    if course is None:
        return Response({"message":"please enter course name "},status=status.HTTP_400_BAD_REQUEST)
    try:
        student = Student.objects.get(admission_id=stu_id)
        try : 
            tuition_fee = Fee.objects.get(fee_name=fee_type)
            print(type(student.degree)) 
            payment = Payment.objects.create(payment_method='cash',amount_paid=100,student=student,course=student.degree)
            date = payment.done_at.date()
            time = payment.done_at.time()
            return Response({'transaction_id':payment.txn_id,'date_created':date,'time(UTC)':time},status=status.HTTP_202_ACCEPTED)
        except Fee.DoesNotExist:
            return Response({"message":"this fee type is not avaiable for this course"},status=status.HTTP_400_BAD_REQUEST)
           
    except Student.DoesNotExist:
        return Response({"message":"student does not exists"},status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def all_transactions(request):
    

    student_id = request.query_params.get('admission_id',None)
    if student_id is None:
        paginator = PageNumberPagination()
        paginator.page_size = 10
        response_dict = { 
                'all_transactions':[],

            }
        
        payments = Payment.objects.all()
        for payment in payments:

            dct = { 'student_details': {},
                    'course_details':{}
            
                  }
            payment.student.payment_approved=True
            payment.student.save()
            dct['course_details']['txn_id']=(payment.txn_id)
            dct['course_details']['amount_paid']=(payment.amount_paid)
            dct['course_details']['fee_type'] = payment.fee.fee_name
            dct['student_details']['admission_id']=payment.student.admission_id
            dct['student_details']['email']=(payment.student.user.email)
            dct['course_details']['degree'] = payment.student.degree.name
            dct['course_details']['payment_method'] = payment.payment_method
            response_dict['all_transactions'].append(dct)
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