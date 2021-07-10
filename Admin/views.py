import datetime

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from .serializers import *
from user.models import User
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework import generics, status
from App.models import product
import uuid


# Create your views here.
class registeradminapi(APIView):
    def post(self, request):
        serializer = admin_serializer(data=self.request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            username = uuid.uuid4().hex[:8].upper()
            print(username)
            passwords = uuid.uuid4().hex[:8].upper()
            print(passwords)

            user_query = User.objects.create_user(username=username,
                                                  password=passwords, is_amazon_admin=True)
            admin_query = serializer.save(user=user_query,unique_id=username,unique_password=passwords)
            register_query = amazon_admin_notification.objects.create(amazon_admin=admin_query)
            Admin_query = serializer.save(amazon_admin_notification=register_query)
            print(Admin_query)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})


class adminapilist(RetrieveUpdateAPIView):
    queryset = Amazon_Admin.objects.all()
    serializer_class = admin_serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        query = self.request.user
        print(query.id)
        admin_detail = Amazon_Admin.objects.filter(user=query.id,Active=False)
        serializer = admin_serializer(admin_detail, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        query = self.request.user
        print(query.id)
        instance = Amazon_Admin.objects.get(user=query.id)
        print(instance.id, instance.unique_id)
        serializer = admin_serializer(instance, data=request.data)
        # print(serializers)
        if serializer.is_valid(raise_exception=True):
            message = "your profile is updated, here is your unique id {}".format(instance.unique_id)
            Query = amazon_admin_notification.objects.create(amazon_admin=instance, message=message)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors)


class notificationlist(ListAPIView):
    queryset = amazon_admin_notification.objects.all()
    serializer_class = Amazon_Admin_Notificartions_Serializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def list(self, request, *args, **kwargs):
        query = (self.request.user)
        print(query.id)
        Query = amazon_admin_notification.objects.filter(amazon_admin=query.id)
        Query.update(seen=True,updated_at=datetime.datetime.now(), created_at =datetime.datetime.now())
        serializer = Amazon_Admin_Notificartions_Serializer(Query, many=True)
        return Response(serializer.data)


class countunseen_notification(ListAPIView):
    queryset = amazon_admin_notification.objects.all()
    serializer_class = Amazon_Admin_Notificartions_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        query = (self.request.user)
        Query = amazon_admin_notification.objects.filter(amazon_admin=query.id,seen=False).count()
        print(Query)
        return Response({"count":Query})
class checksuperuserapi(RetrieveUpdateAPIView):
    queryset = Amazon_Admin.objects.all()
    serializer_class = admin_serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
                admin_detail = Amazon_Admin.objects.filter(user=self.kwargs["pk"])
                serializer = admin_serializer(admin_detail, many=True)
                print(serializer.data)

                return Response(serializer.data)
        else:
                return Response("YOU ARE NOT SUPER USER")
    def update(self, request, *args, **kwargs):
      if self.request.user.is_superuser:
        instance = Amazon_Admin.objects.get(user=self.kwargs["pk"])
        serializer = checksuperuserapiserializer(instance,data=request.data)
        # print(serializers)
        instances = Amazon_Admin.objects.get(user=self.kwargs['pk'])
        print(instances.id, instances.unique_id,instances.unique_password)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            query = self.request.data['Active']
            print(query)
            if query == 'True':
             amazon_admin_notification.objects.create(amazon_admin=instance, message="your account is activated and your unique is {} and password is{}".format(instances.unique_id,instances.unique_password))

            else:
               amazon_admin_notification.objects.create(amazon_admin=instance, message="your account is not activated")
#
            return Response(serializer.data, status=status.HTTP_200_OK)

      else:
          return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
class ratingbyadminapi(ListCreateAPIView):
    queryset = products.objects.all()
    serializer_class = ratingserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer, *args, **kwargs):
        product_id = serializer.validated_data.get('product')
        serializer.save()
        print(product_id, type(product_id), product_id.id)

        rating_list = []
        product_review={}
        j = 0
        k=0
        for i in products.objects.filter(product=product_id.id):
           j = i.rating + j
           print(i.Admin.id)
           Query=Amazon_Admin.objects.get(id=i.Admin.id)
           print(Query.first_name)
           product_review[Query.first_name]=i.review
           print(product_review)
           rating_list.append(i.rating)
           count = len(rating_list)

           formula = j / count
           app_query = product.objects.get(id=product_id.id)
           app_query.overall_rating = formula
           app_query.overall_review=product_review
           app_query.save()



