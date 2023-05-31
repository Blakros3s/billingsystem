from django.shortcuts import render, redirect

# Create your views here.
def homepage(request):
    return render(request,'layouts/home.html')