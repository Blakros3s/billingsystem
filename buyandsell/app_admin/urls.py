from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.adminpage, name="adminpage"),
    path('user/add', views.add_user, name="add-user"),
    path('user/', views.list_user, name="list-user"),
    path('user/delete/<int:id>/', views.delete_user, name='delete-user'),
    path('bill/', views.bill_list, name='all-bill'),
    path('bill/view/<int:id>/', views.bill_view, name='show-bill'),
    path('earning/', views.earning_list, name='list-earning'),
]