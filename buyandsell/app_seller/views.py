from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def sellerpage(request):
    return render(request, 'seller/dashboard.html')

def product_add(request):
    if request.method == "POST":

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

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
     }
    return render(request, 'seller/list_product.html', context)

def product_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('list-product')

def product_edit(request, id):
    product = Product.objects.get(id=id)
    context = {"product": product}
    return render(request, 'seller/edit_product.html', context)

def product_update(request):
    if request.method == "POST":
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