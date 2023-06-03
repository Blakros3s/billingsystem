from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.adminpage, name="adminpage"),
    path('user/add', views.add_user, name="add-user"),
    path('user/', views.list_user, name="list-user"),
    path('user/delete/<int:id>/', views.delete_user, name='delete-user'),
]