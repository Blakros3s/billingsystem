from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from app_buyer.models import *
import random

# Create your views here.
# Check if the user is authenticated and has the seller role
def is_seller(user):
    return user.is_authenticated and user.is_seller


@login_required(login_url='/login/')
@user_passes_test(is_seller)
def sellerpage(request):
    # Render the seller dashboard page
    return render(request, 'seller/dashboard.html')


@login_required(login_url='/login/')
@user_passes_test(is_seller)
def product_add(request):
    if request.method == "POST":
        # Create a new Product object and populate its fields with the form data
        product = Product()
        product.title = request.POST.get('title')
        product.desc = request.POST.get('desc')
        product.category = request.POST.get('category')
        product.price = request.POST.get('price')
        product.image = request.FILES.get('image')
        product.user = request.user
        product.save()
        return redirect('add-product')
    return render(request, 'seller/add_product.html')



@login_required(login_url='/login/')
@user_passes_test(is_seller)
def product_list(request):
    # Get all products associated with the seller from the database
    products = Product.objects.filter(user__username=request.user.username)
    context = {
        'products': products
     }
    return render(request, 'seller/list_product.html', context)


@login_required(login_url='/login/')
@user_passes_test(is_seller)
def product_delete(request, id):
    # Get the product with the specified id from the database
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('list-product')


@login_required(login_url='/login/')
@user_passes_test(is_seller)
def product_edit(request, id):
    # Get the product with the specified id from the database
    product = Product.objects.get(id=id)
    context = {"product": product}
    return render(request, 'seller/edit_product.html', context)


def product_update(request):
    if request.method == "POST":
        # update the product object and populate its fields with the form data
        product_id = request.POST.get('id')
        product = Product.objects.get(id=product_id)
        product.title = request.POST.get('title')
        product.desc = request.POST.get('desc')
        product.category = request.POST.get('category')
        product.price = request.POST.get('price')
        
        # Check if a new image was provided
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        
        product.save()
        return redirect('list-product')
    return redirect('list-product')


@login_required(login_url='/login/')
@user_passes_test(is_seller)
def order_list(request):
    # Get all purchases/orders associated with the seller from the database
    purchase = Purchase.objects.filter(seller_username=request.user.username)
    context = {
        'purchase': purchase
     }
    return render(request, 'seller/list_order.html', context)


@login_required(login_url='/login/')
@user_passes_test(is_seller)
# Generate a bill for a specific purchase
def bill_generate(request, id):
    purchase = Purchase.objects.get(id=id)
    context = {
        'purchase': purchase
     }
    return render(request, 'seller/generate_bill.html', context)



def bill_update(request):
    if request.method == "POST":
        # Create a new Bill object and populate its fields with the form data
        bill = Bill()
        bill.item = request.POST.get('item')
        bill.amount = request.POST.get('amount')
        bill.category = request.POST.get('category')
        bill.seller_name = request.POST.get('seller')
        bill.customer_name = request.POST.get('buyer')
        bill.order_no = request.POST.get('order_no')
        bill.invoice_no = random.randint(10000000,100000000)
        bill.save()
        return redirect('list-order')
    return redirect('list-order')


@login_required(login_url='/login/')
@user_passes_test(is_seller)
# List all bills for the seller
def bill_list(request):
    bills = Bill.objects.filter(seller_name=request.user.get_full_name())
    context = {
        'bills': bills
     }
    return render(request, 'seller/list_bill.html', context)


@login_required(login_url='/login/')
@user_passes_test(is_seller)
# View the details of a specific bill
def bill_view(request, id):
    bill = Bill.objects.get(id=id)
    excluding_vat = float(bill.amount) / 1.13
    context = {
        'bill': bill, 'excluding': excluding_vat
     }
    return render(request, 'seller/view_bill.html', context)