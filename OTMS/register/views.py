from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.hashers import make_password


def main_page(request):
    """
    Displays the main page of your web application.
    """
    return render(request, 'global/main.html')

def register_users(request):
    """
    Implements user registration functionality. If the request is a POST request, an instance of
    CustomUserCreationForm is created with data from the request. The form is then checked for validity. If the form passes
    the validation, a new user is created, and the user's password is hashed for secure storage. 
    After a successful registration, the user is automatically logged into the system. The user is then redirected to the main page.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        request_copy = request.POST.copy()
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        request_copy[password1] = password1
        request_copy[password2] = password2
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register/register_users.html', {'form': form})
