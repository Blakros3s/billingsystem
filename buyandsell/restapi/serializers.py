from rest_framework import serializers
from app_buyer.models import *
from app_seller.models import *
from authentication.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'is_admin', 'is_seller', 'is_buyer']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Product
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'
