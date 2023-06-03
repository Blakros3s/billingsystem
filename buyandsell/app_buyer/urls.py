from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.buyerpage, name="buyerpage"),
    path('products/', views.all_product, name='all-product'),
    path('products/view/<int:id>/', views.view_product, name='view-product'),
    path('payment/<int:id>/', views.payment, name='payment'),
    path('payment/purchased', views.payment_update, name='update-payment'),

]