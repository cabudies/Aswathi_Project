
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
