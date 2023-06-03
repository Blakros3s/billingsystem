from django.db import models

# Create your models here.
class Purchase(models.Model):
    item = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    seller = models.CharField(max_length=200)
    seller_username = models.CharField(max_length=200)
    buyer = models.CharField(max_length=200, default=None)
    buyer_username = models.CharField(max_length=200, default=None)
    order_no = models.CharField(max_length=200, unique=True, default=None)
    def __str__(self):
        return self.item