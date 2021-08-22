from django.shortcuts import render
from . import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny ,IsAuthenticated , IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView , ListAPIView , CreateAPIView , UpdateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny ,IsAuthenticated , IsAdminUser
from .models import HeadOfDepartment
from rest_framework import status

class HodLoginView(TokenObtainPairView):
    permission_classes  = [AllowAny,]
    serializer_class = serializers.HodObtainPairSerializer

class EditHodProfile(CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = serializers.EditHodProfileSerializer
    queryset = HeadOfDepartment.objects.all()

    def create(self , request,*args , **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'message':'details updated',}, status=status.HTTP_201_CREATED,)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ViewHodProfile(ListCreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = serializers.ViewHodProfileSerializer
    queryset = HeadOfDepartment.objects.all()
    # lookup_field = 'user'

    # def get(self , request,*args , **kwargs):
    #     # serializer = self.get_serializer(data=request.data)
    #     # print("Serializer for view hod details=======", serializer.data)
    #     # return Response(serializer.data, status=status.HTTP_200_OK)
    #     queryset = HeadOfDepartment.objects.all()
    #     # queryset = self.get_queryset()
    #     obj = get_object_or_404(queryset, user=self.request.user)
    #     print("obj=======", obj)
    #     return obj


    #     # serializer = self.get_serializer(data=request.data)
        
    #     # if serializer.is_valid():
    #     #     self.perform_create(serializer)
    #     #     return Response({'message':'details updated',}, status=status.HTTP_201_CREATED,)
    #     # else:
    #     #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

