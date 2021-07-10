#from django.shortcuts import render
from rest_framework.response import Response
#from datetime import date, datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from  rest_framework.views import APIView
from .serializers import *
from rest_framework.generics import ListAPIView
from rest_framework import generics, status

# Create your views here.

class RegisterUser(APIView) :
    def post(self,request):
      serializer=userseializer(data=request.data)

      if serializer.is_valid(raise_exception=True):
        serializer.save()
      #  user=User.objects.get(username=serializer.data['username'])
        return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong',})
# Create your views here.
class Userapi(ListAPIView):
    queryset = User.objects.all()
    serializer_class = userseializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]