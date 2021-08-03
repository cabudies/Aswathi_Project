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
from .models import Fee , Degree

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def all_transactions(request):
    return Response(
        {
            "message" : "Your payment was not successfull"
        },
        status = status.HTTP_202_ACCEPTED
    )