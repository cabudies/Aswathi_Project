from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView , RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view , permission_classes
from .models import Degree
from . import serializers
from rest_framework.response import Response
  

@api_view(['GET'])
@permission_classes([AllowAny,])
def CourseDetails(request):
    name = request.query_params.get('name')
    print(name)
    try:
        degree = Degree.objects.get(name=name)
        serializer = serializers.CourseSerializer(degree)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    except:
        return Response({"message": "This Course Does Not Exists"},status=status.HTTP_400_BAD_REQUEST)