from django.urls import path
from .views import *
urlpatterns = [

path('userapiviewofcustomer',userapi.as_view()),
    ]