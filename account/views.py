from django.shortcuts import render, redirect
from .models import Userregistration
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method == "POST":
        form = request.POST
        username = form.get('username')
        email = form.get('email')
        mobile = form.get('mobile')
        password = form.get('password')
        if Userregistration.objects.filter(email=email).exists():
            messages.warning(request, "Email already exist")
            return redirect('signup')
        else:
            userdata = Userregistration(username=username, email= email, mobile= mobile, password= password)
            userdata.password = make_password(userdata.password)
            userdata.register()
            return redirect("login")
    else:
         return render(request, "account/signup.html")
    return render(request, "account/signup.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_login = Userregistration.user_email(email)
        if user_login:
            user_p = check_password(password,user_login.password)
            if user_p:
                request.session["user_id"] = user_login.id
                request.session["email"] =  user_login.email
                return redirect("/")
        else:
            messages.warning(request, "Email or Password is incorrect")
    else:
         return render(request, "account/login.html")
        # messages.warning(request, "Email or password is invalid")
   
    return render(request, "account/login.html")

def logout(request):
    request.session.flush()
    return redirect('/')