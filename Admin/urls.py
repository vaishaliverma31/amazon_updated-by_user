from django.urls import path
from .views import *
urlpatterns = [

path('registeration_of_admin',registeradminapi.as_view()),
path('adminapilist/',adminapilist.as_view()),
path('Amazon_Admin_notification_View/',notificationlist.as_view()),
path('countunseen_notification',countunseen_notification.as_view()),
path('checksuperuserapi/<int:pk>',checksuperuserapi.as_view()),
path('rating_by_admin',ratingbyadminapi.as_view())
]