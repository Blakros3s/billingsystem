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
    
class Bill(models.Model):
    item = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    order_no = models.CharField(max_length=200, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_no = models.CharField(max_length=200, unique=True)
    customer_name = models.CharField(max_length=100)
    seller_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.invoice_no