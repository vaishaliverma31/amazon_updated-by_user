from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class product(models.Model):
    product_name=models.CharField(max_length=120,unique=True)
    overall_rating=models.FloatField(null=True)
    overall_review=models.CharField(max_length=200,null=True,)
    def __str__(self):
        return self.product_name