import uuid

from django.db import models
from django.db import models
from localflavor.in_.models import INStateField
from django.core.validators import MinValueValidator,MaxValueValidator
from datetime import date

from io import BytesIO
#from PIL import Image, ImageDraw




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
class Amazon_Admin(models.Model):
    user = models.OneToOneField("user.User", on_delete=models.CASCADE, null=True, blank=True)
    password = models.CharField(max_length=300, null=True, unique=True)
    unique_id = models.CharField(max_length=200, unique=True, editable=False,null=True)
    unique_password=models.CharField(max_length=200, unique=True, editable=False,null=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True,default=False)
    last_name = models.CharField(max_length=200)
    DOB = models.DateField(default=date.today)
    gender = models.CharField(max_length=10, choices=gender_choices)
    id_proof = models.CharField(max_length=30, choices=id_proof)
    gender = models.CharField(max_length=10, choices=gender_choices)
    state = INStateField(null=True, blank=True,default=False)
    Active=models.BooleanField(default=False)
class amazon_admin_notification(models.Model):
    amazon_admin = models.ForeignKey(Amazon_Admin, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class products(models.Model):
    Admin=models.ForeignKey(Amazon_Admin,on_delete=models.CASCADE,null=True)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    review = models.CharField(max_length=200)
    product = models.ForeignKey("App.product", on_delete=models.CASCADE)