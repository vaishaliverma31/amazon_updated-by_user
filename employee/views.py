
from Admin.models import Amazon_Admin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from .serializers import *
from user.models import User
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView, RetrieveUpdateAPIView,UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from rest_framework import generics, status
class registeremployeeapi(APIView):
    def post(self, request):
        serializer = employee_serializer(data=self.request.data)
       # print(serializer)
        if serializer.is_valid(raise_exception=True):
            user_query = User.objects.create_user(username=self.request.data['first_name'],
                                                  password=self.request.data['password'], is_amazon_employee=True)
            admin_query = serializer.save(user=user_query)
            print(admin_query)
            register_query = amazon_employee_notification.objects.create(amazon_employee=admin_query)
            Admin_query = serializer.save(amazon_employee_notification=register_query)
            print(Admin_query)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})
        # Create your views here.
class notificationlist_employee(ListAPIView):
    queryset = amazon_employee_notification.objects.all()
    serializer_class = Amazon_employee_Notificartions_Serializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request, *args, **kwargs):
        query=self.request.user
        print(query.id)
        Query=amazon_employee_notification.objects.filter(amazon_employee=query.id)
       # print(Query.seen)
        Query.update(seen=True)
        serializer=self.get_serializer(Query,many=True)
        #print(serializer)
        return Response(serializer.data)
class employeeapilist(RetrieveUpdateAPIView):
    queryset = Amazon_employee.objects.all()
    serializer_class = employee_serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def update(self, request, *args, **kwargs):
        query = self.request.user
        print(query.id)
        instance = Amazon_employee.objects.get(user=query.id)
        print(instance.id)
        serializer =employee_serializer(instance, data=request.data)
        # print(serializers)
        if serializer.is_valid(raise_exception=True):
            message = "your profile is updated"
            Query = amazon_employee_notification.objects.create(amazon_employee=instance, message=message)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors)


    def get(self, request, *args, **kwargs):
        query = self.request.user
        print(query.id)
        admin_detail = Amazon_employee.objects.filter(user=query.id,Active=False)
        serializer = employee_serializer(admin_detail, many=True)
        return Response(serializer.data)
class countunseen_notification_of_employee(ListAPIView):
    queryset = amazon_employee_notification.objects.all()
    serializer_class = Amazon_employee_Notificartions_Serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        query = (self.request.user)
        Query = amazon_employee_notification.objects.filter(amazon_employee=query.id,seen=False).count()
        print(Query)
        return Response({"count":Query})
class check_employeeactive_by_admin(RetrieveUpdateAPIView):
    queryset = Amazon_employee.objects.all()
    serializer_class = employee_serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        if self.request.user.is_amazon_admin:
                admin_detail = Amazon_employee.objects.filter(user=self.kwargs["pk"])
                serializer = activeemployee_serializer(admin_detail, many=True)
                print(admin_detail)
                return Response(serializer.data)
        else:
                return Response("YOU ARE NOT Amazon admin")
    def update(self, request, *args, **kwargs):
       if self.request.user.is_amazon_admin:
         query=Amazon_Admin.objects.get(user=self.request.user)
         if query.Active==True:

           instance = Amazon_employee.objects.get(user=self.kwargs["pk"])
           serializer = activeemployee_serializer(instance,data=request.data)
        # print(serializers)
           if serializer.is_valid(raise_exception=True):
             serializer.save()
             query = self.request.data['Active']
             if query == 'True':
                amazon_employee_notification.objects.create(amazon_employee=instance, message="your account is activated")
             else:
               amazon_employee_notification.objects.create(amazon_employee=instance, message="your account is not activated")

             return Response(serializer.data, status=status.HTTP_200_OK)
         else:
             return Response('Admin is not active')
           # print(active)
       else:
             return Response({"NOt A amazon_admin"}, status=status.HTTP_401_UNAUTHORIZED)