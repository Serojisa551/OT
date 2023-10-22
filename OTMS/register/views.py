from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User 
import smtplib
from django.contrib.auth import get_user_model
from random import randint

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
        email = request.POST.get("email")
        if CustomUserCreationForm.email_valid(email) == None:
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('main_page')
        form = CustomUserCreationForm()        
        return render(request, 'register/register_users.html',  {'form': form})
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

def send_email(request):
    """
    Generates a token and sends email
    """
    if request.method == "POST":
        from_email = 'isahakyan2021@gmail.com'
        to_email = request.POST.get("email")
        app_password = 'ksacudajkxovanqn'
        try:
            token = generated_token()
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(from_email, app_password)
            server.sendmail(from_email, to_email, token)
            server.quit()
            print("Email sent successfully!")
            return redirect(f"/checking_email/{token}/?email={to_email}")
        except Exception as e:
            print(f"Error: {e}")
    return render(request, 'register/password_reset/email_password_reset.html')

def checking_email(request, token):
    """
    If it passes the token check, it goes to the password reset page, if it does not pass, then the update form.
    """
    if request.method == "POST":
        origin_token = token
        user_token = request.POST.get("token")
        if origin_token == user_token:
            email = request.GET.get("email")
            return redirect(f"/password_reset/{email}/")
    return render(request, "register/password_reset/checking_email.html")

def reset_password(request, email):
    """
    If the request method is POST, the function tries to find the user with the specified email.
    If the user is not found, he is redirected to the password reset page.
    Otherwise, the user's password is changed to the new password specified in the POST request.
    After a successful password reset, the user is redirected to the authentication page.
    """
    if request.method == "POST":
        try:
            users = get_user_by_email(email)
            if users == None:
                return redirect("password_reset_email")
            else:
                user = User.objects.get(pk=users.pk)
                user.set_password(request.POST.get("password1"))
                print("befor save", request.POST.get("password1"))
                user.save()
                print("after save")
                return redirect('authentic_user')
        except User.DoesNotExist as e:
            print(f"Error: {e}")
    return render(request,"register/password_reset/reset_password.html")

def get_user_by_email(email):
    """
    The function tries to find the user by the specified email.
    If a user with such mail is found, it is returned as a user object.
    If the user is not found, the function returns None.
    """
    User = get_user_model()
    try:
        user = User.objects.get(email=email)
        print(user)
        return user
    except User.DoesNotExist:
        print(None)
        return None

def generated_token():
    token = ""
    for i in range(6):
        token += str(randint(0,10))
    return token