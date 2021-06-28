from django.shortcuts import render
from . import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny ,IsAuthenticated , IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView



class HrLoginView(TokenObtainPairView):
    permission_classes  = [AllowAny,]
    serializer_class = serializers.HrObtainPairSerializer