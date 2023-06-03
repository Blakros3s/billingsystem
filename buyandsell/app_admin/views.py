from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from authentication.models import CustomUser

# Create your views here.
def adminpage(request):
    return render(request, 'admin/dashboard.html')

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


def list_user(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
     }
    return render(request, 'admin/list_user.html', context)

def delete_user(request, id):
    user = CustomUser.objects.get(id=id)
    user.delete()
    return redirect('list-user')