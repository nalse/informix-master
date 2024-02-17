from django.shortcuts import render,redirect
from pages.models import Pages
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.conf import settings
from results.models import Result

# Create your views here.
def register(request):
    pages = Pages.objects.last()
    content ={
        "pages":pages
    } 
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username   = request.POST['username']
        email      = request.POST['email']
        password   = request.POST['password']
        password1  = request.POST['password1']
        if password == password1: 
            if User.objects.filter(username = username).exists():
                messages.error(request, "Bu istifadəçi adı artıq mövcuddur")
                return redirect(register)
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request,"bu email artiq mövcuddur")
                    return redirect(register)
                else:
                    user =User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                    auth.login(request, user)
                    messages.success(request,"Qeydiyyatiniz uğurla başa çatdi")  
                    return redirect('index')
        else:
            messages.error(request,"Şifrələrdə uyğunluq pozulub")
            return redirect(register)

    else:
        return render(request,'account/register.html',content)

def login(request):
    pages = Pages.objects.last()
    content ={
        "pages":pages
    }
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        try:
            remember = request.POST['remember_me']
            if remember:
                settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
        except:
            is_private = False
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'Yanlışdır! Yenidən cəhd edin')
            return redirect('login')
    else:
         return render(request,'account/login.html',content)

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request,'Siz indi çıxış etdiniz')
        return redirect('index')

def dashboard(request):
    pages = Pages.objects.last()
    results = Result.objects.all()
    content ={
        "pages":pages,
        "results":results
    } 
    return render(request, 'account/dashboard.html',content)





