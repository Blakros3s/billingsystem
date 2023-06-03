from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import update_session_auth_hash
from authentication.models import CustomUser
from app_seller.models import *
# Create your views here.
def is_admin(user):
    return user.is_authenticated and user.is_admin

@login_required(login_url='/login/')
@user_passes_test(is_admin)
def adminpage(request):
    return render(request, 'admin/dashboard.html')

@login_required(login_url='/login/')
@user_passes_test(is_admin)
def add_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        # Create a new user with the given details
        user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        if user_type == 'admin':
            user.is_admin = True
        elif user_type == 'seller':
            user.is_seller = True
        elif user_type == 'buyer':
            user.is_buyer = True
        user.save()
    
    return render(request, 'admin/add_user.html')

@login_required(login_url='/login/')
@user_passes_test(is_admin)
def list_user(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
     }
    return render(request, 'admin/list_user.html', context)

@login_required(login_url='/login/')
@user_passes_test(is_admin)
def delete_user(request, id):
    user = CustomUser.objects.get(id=id)
    user.delete()
    return redirect('list-user')


@login_required(login_url='/login/')
@user_passes_test(is_admin)
def bill_list(request):
    bills = Bill.objects.all()
    context = {
        'bills': bills
     }
    return render(request, 'admin/list_bill.html', context)


@login_required(login_url='/login/')
@user_passes_test(is_admin)
def bill_view(request, id):
    bill = Bill.objects.get(id=id)
    excluding_vat = float(bill.amount) / 1.13
    context = {
        'bill': bill, 'excluding': excluding_vat
     }
    return render(request, 'admin/view_bill.html', context)


@login_required(login_url='/login/')
@user_passes_test(is_admin)
def calculate_lifetime_earnings(bills):
    lifetime_earnings = {}
    
    for bill in bills:
        seller_name = bill.seller_name
        amount = bill.amount
        
        if seller_name in lifetime_earnings:
            lifetime_earnings[seller_name] += amount
        else:
            lifetime_earnings[seller_name] = amount
    print(lifetime_earnings)
    return lifetime_earnings


@login_required(login_url='/login/')
@user_passes_test(is_admin)
def earning_list(request):
    bills = Bill.objects.all()
    lifetime_earnings = calculate_lifetime_earnings(bills)
    context = {'lifetime_earnings': lifetime_earnings}
    return render(request, 'admin/list_earning.html', context)

