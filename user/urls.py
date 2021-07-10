from django.urls import path
from .views import *
urlpatterns = [

path('registeration',RegisterUser.as_view()),
path('Userapilist/',Userapi.as_view())
]
