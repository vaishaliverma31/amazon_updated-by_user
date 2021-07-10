from rest_framework import serializers
from .models import *

class admin_serializer(serializers.ModelSerializer):
    class Meta:
        fields=['first_name','password','DOB','last_name','gender','id_proof','state','Active','unique_id','unique_password']
        model= Amazon_Admin
class Amazon_Admin_Notificartions_Serializer(serializers.ModelSerializer):
    class Meta:
        model = amazon_admin_notification
        fields = '__all__'
class checksuperuserapiserializer(serializers.ModelSerializer):
    class Meta:
        fields=['Active']
        model= Amazon_Admin
class ratingserializer(serializers.ModelSerializer):
    class Meta:
       fields=['product','review','rating','Admin']
       model=products