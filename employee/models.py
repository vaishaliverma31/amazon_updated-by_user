from django.db import models
from localflavor.in_.models import INStateField
from django.db import models
from datetime import date, datetime

# Create your models here.
gender_choices = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)
id_proof = (
    ("Aadhar Card", "Aadhar Card"),
    ("Pan Card", "Pan Card"),
)
class Amazon_employee(models.Model):
    user = models.OneToOneField("user.User", on_delete=models.CASCADE, null=True, blank=True)
    password = models.CharField(max_length=300, null=True, unique=True,)
    unique_id = models.CharField(max_length=200, unique=True, editable=False, null=True, blank=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200)
    DOB = models.DateField(default=date.today)
    gender = models.CharField(max_length=10, choices=gender_choices)
    id_proof = models.CharField(max_length=30, choices=id_proof)
    gender = models.CharField(max_length=10, choices=gender_choices)
    state = INStateField(null=True, blank=True)
    Active=models.BooleanField(default=False)
class amazon_employee_notification(models.Model):
    amazon_employee = models.ForeignKey(Amazon_employee, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)