from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib import messages
# Create your views here.

# Define the LoginView class which handles the /login endpoint
class LoginView(View):
    # Handles HTTP GET requests
    def get(self, request):
        return render(request,'authentication/login.html')
    
    # Handles HTTP POST requests
    def post(self, request):
        # Retrieve the username and password submitted in the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user using the Django auth module
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # Redirect the user to the appropriate page based on their usertype
            if user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user.is_seller:
                login(request, user)
                return redirect('sellerpage')
            elif user.is_buyer:
                login(request, user)
                return redirect('buyerpage')
            #else:
        #messages.error(request, "Invalid login credentials. Please try again.")
        # Redirect the user back to the login page
    
        return redirect('login')



class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You've Successfully Logged Out!")
        return redirect('login')
    
