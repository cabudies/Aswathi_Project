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


@api_view(["GET","POST"])
@permission_classes([IsAuthenticated,])
def approve_student(request):

    pk = request.data.get('admission_id')
    try:
        student = Student.objects.get(admission_id=pk)
        #user = CustomUser.objects.get(id=pk)
        if student.payment_approved == True:
            student.student_approved = True
            student_mail = student.user.email
            student_name = student.user.first_name  
            #subject = "Login Credentials"
            #message = "Hello Your Login credentials your email"
            #recepient = str(user.email)
            #send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            data = {'message':'Student Approved','name':student_name,'email':student_mail}
            return Response(data)
        else:
            data = {'message':"student's payment is not approved.please contact accountant."}
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
    except Student.DoesNotExist:
        return Response({"message":"student with given id does not exists"},status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def cash_payments(request):
    

    student_id = request.data.get('admission_id',None)
    if student_id is None:
        paginator = PageNumberPagination()
        paginator.page_size = 10
        response_dict = { 
                'cash_transactions':[],

            }
        
        payments = Payment.objects.filter(payment_method='cash')
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
            response_dict['cash_transactions'].append(dct)
        return Response(response_dict,status=status.HTTP_202_ACCEPTED)
    elif student_id is not None:
        paginator = PageNumberPagination()
        paginator.page_size = 10
        response_dict = { 
                'cash_transactions':[],

            }
        try:
            student = Student.objects.get(admission_id=student_id)
            payments = Payment.objects.filter(payment_method='cash',student=student)
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
                response_dict['cash_transactions'].append(dct)
            return Response(response_dict,status=status.HTTP_202_ACCEPTED)
        except Student.DoesNotExist:
            return Response({'message':"student with this given id does not exists"})

    else:

        return Response({

           "Message":"Not a valid query."

        },status=staus.HTTP_400_BAD_REQUEST)