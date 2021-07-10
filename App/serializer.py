from rest_framework import serializers
from .models import *

class productserializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ['product_name','overall_rating','overall_review']
