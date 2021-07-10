from django.shortcuts import render
from user.models import User
from user.serializers import userseializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from django.core.paginator import Paginator
#class pagination(LimitOffsetPagination):
   # default_limit = 3
 #   max_limit = 5
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class userapi(ListAPIView):
        queryset = User.objects.all()
        serializer_class = userseializer
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]

        def get(self, request, *args, **kwargs):
            if self.request.user.is_amazon_admin or self.request.user.is_amazon_employee or self.request.user.is_amazon_employee:
                 query = self.request.user
                 print(query.id)

                 admin_detail = User.objects.filter( is_amazon_admin=False,is_amazon_employee=False, is_amazon_customer=True)
                 serializer = userseializer(admin_detail, many=True)


                 return Response(serializer.data)
            return Response("'can't respond")