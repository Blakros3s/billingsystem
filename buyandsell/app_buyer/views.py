from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from app_seller.models import Product
from .models import *
import random

# Create your views here.
def is_buyer(user):
    return user.is_authenticated and user.is_buyer


@login_required(login_url='/login/')
@user_passes_test(is_buyer)
def buyerpage(request):
    return render(request, 'buyer/dashboard.html')


@login_required(login_url='/login/')
@user_passes_test(is_buyer)
def all_product(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'buyer/all_product.html', context)


@login_required(login_url='/login/')
@user_passes_test(is_buyer)
def view_product(request, id):
    product = Product.objects.get(id=id)
    context = {"product": product} 
    return render(request, 'buyer/view_product.html', context)


@login_required(login_url='/login/')
@user_passes_test(is_buyer)
def payment(request,id):
    product = Product.objects.get(id=id)
    context = {"product": product} 
    return render(request, 'buyer/payment.html',context)


@login_required(login_url='/login/')
@user_passes_test(is_buyer)
def payment_update(request):
    if request.method == "POST":
        purchase = Purchase()
        purchase.item = request.POST.get('title')
        purchase.amount = request.POST.get('price')
        purchase.category = request.POST.get('category')
        purchase.seller = request.POST.get('seller')
        purchase.seller_username = request.POST.get('seller_username')
        purchase.buyer = request.POST.get('buyer')
        purchase.buyer_username = request.POST.get('buyer_username')
        purchase.order_no = random.randint(1000000,10000000)
        purchase.save()
        return redirect('all-product')
    return redirect('all-product')
