from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import  *
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class productapi(ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = productserializer
   # authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated]
