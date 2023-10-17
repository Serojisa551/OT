from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User 

def main_page(request):
    """
    Displays the main page of your web application.
    """
    user = request.user
    return render(request, 'global/main.html', {'users': user})

def register_users(request):
    """
    Implements user registration functionality. If the request is a POST request, an instance of
    CustomUserCreationForm is created with data from the request. The form is then checked for validity. If the form passes
    the validation, a new user is created, and the user's password is hashed for secure storage. 
    After a successful registration, the user is automatically logged into the system. The user is then redirected to the main page.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register/register_users.html', {'form': form})

def authentic_user(request):
    """
    This function processes user authentication. It takes a POST request with user credentials
    and validates them using the provided form. If the form is valid and the credentials are correct,
    the user is logged in and redirected to the main page of the application. If the credentials are
    incorrect, an error message is displayed on the login page.
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  
                return redirect("main_page")
            else:
                messages.error(request, "Invalid username or password.") 
    form = AuthenticationForm()
    return render(request, "register/login_users.html", {"login_form": form})

def logout_request(request):
    """
    Logs out the currently logged-in user and redirects to the login page.
    """
    logout(request) 
    return redirect('main_page')