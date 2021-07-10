from rest_framework import serializers
from .models import *

class employee_serializer(serializers.ModelSerializer):
    class Meta:
        fields=['first_name','password','DOB','last_name','gender','id_proof','state','Active',]
        model= Amazon_employee
class Amazon_employee_Notificartions_Serializer(serializers.ModelSerializer):
    class Meta:
        model = amazon_employee_notification
        fields = '__all__'
class activeemployee_serializer(serializers.ModelSerializer):
    class Meta:
        fields=['Active']
        model= Amazon_employee