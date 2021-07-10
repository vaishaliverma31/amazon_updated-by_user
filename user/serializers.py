from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User=get_user_model()


class userseializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username','password','is_amazon_admin','is_amazon_employee','is_amazon_customer']