from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

def loginUser(request):
   if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")

      user = authenticate(username=username, password=password)
      remember = request.POST.get("rememberme")
      if user is not None:
         login(request, user)
         messages.success(request, "Giriş Yaptınız...")
         if remember:
            request.session.set_expiry(604800)
         return redirect("indexPage")
      else:
         messages.error(request, "Kullanıcı adı veya şifre hatalı!")
   context={}
   return render(request, 'user/login.html', context)


@login_required(login_url="loginUser")
def logoutUser(request):
   # if request.user.is_authenticated:
   logout(request)
   return redirect("loginUser")

def registerUser(request):
   # email kontrol doğrulama
   # password kontrol
   # satıcı mı, normal mi
   context={}
   return render(request, 'user/register.html', context)
