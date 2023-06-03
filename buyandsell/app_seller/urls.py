from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.sellerpage, name="sellerpage"),
    path('product/add/', views.product_add, name='add-product'),
    path('product/', views.product_list, name='list-product'),
    path('product/edit/<int:id>/', views.product_edit, name='edit-product'),
    path('product/update/', views.product_update, name='update-product'),
    path('product/delete/<int:id>/', views.product_delete, name='delete-product'),
    path('order/', views.order_list, name='list-order'),
    path('bill/generate/<int:id>/', views.bill_generate, name='generate-bill'),
    path('bill/generated/', views.bill_update, name='update-bill'),
    path('bill/', views.bill_list, name='list-bill'),
    path('bill/view/<int:id>/', views.bill_view, name='view-bill'),
]