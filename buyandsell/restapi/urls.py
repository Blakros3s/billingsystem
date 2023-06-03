from django.urls import path
from .views import *

urlpatterns = [
    path('order/', OrderList.as_view(), name='order-list'),
    path('order/<int:id>/', OrderDetail.as_view(), name='order-detail'),
    path('product/', ProductList.as_view(), name='product-list'),
    path('product/<int:id>/', ProductDetail.as_view(), name='product-detail'),
    path('bill/', BillList.as_view(), name='bill-list'),
    path('bill/<int:id>/', BillDetail.as_view(), name='bill-detail'),
]