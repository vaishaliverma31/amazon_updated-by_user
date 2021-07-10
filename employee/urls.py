from django.urls import path
from .views import *
urlpatterns = [


path('registeration_of_employee',registeremployeeapi.as_view()),
path('adminapilist/', notificationlist_employee.as_view()),
path('notification_of employee',notificationlist_employee.as_view()),
path('_updateandget_of_own_data_by_employee',employeeapilist.as_view()),
path('count_unseen_notification',countunseen_notification_of_employee.as_view()),
path('updated_by_admin/<int:pk>',check_employeeactive_by_admin.as_view()),

    ]