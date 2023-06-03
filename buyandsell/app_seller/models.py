from django.db import models
from authentication.models import CustomUser
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.FileField(null=True, blank=True, upload_to="products/")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title