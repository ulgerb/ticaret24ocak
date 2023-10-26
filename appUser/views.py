from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from ticaret24ocak.settings import EMAIL_HOST_USER
from .models import *

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
   
   if request.method == "POST":
      username = request.POST.get("username")
      fname = request.POST.get("fname")
      lname = request.POST.get("lname")
      email = request.POST.get("email")
      password1 = request.POST.get("password1")
      password2 = request.POST.get("password2")
      char = "-_."
      bool_len = bool_up = bool_num = bool_char = bool_user = bool_email = False
      
      if password1 == password2:
         if len(password1)>=6:
            bool_len = True
         else:
            messages.error(request, 'Şifrenin 6 hane veya daha uzun olması gerekli !')
            
         for i in password1: # 1asd-2
            if i.isupper(): bool_up = True
            if i.isnumeric(): bool_num = True
            if i in char: bool_char = True
            
         if not bool_up:
            messages.error(request, "Şifrede en az bir büyük harf olmalı !")
         if not bool_num:
            messages.error(request, "Şifrede en az bir numara olmalı !")
         if not bool_char:
            messages.error(request, "Şifrede en az bir -_. olmalı !")
         if not User.objects.filter(username=username).exists(): # []
            bool_user = True
         else:
            messages.error(request, "Bu kullanıcı adı zaten kullanılıyor !")
         if not User.objects.filter(email=email).exists(): # []
            bool_email = True
         else:
            messages.error(request, "Bu email zaten kullanılıyor !")

            # anasayfa profile sepet detay
         if bool_len and bool_up and bool_num and bool_char and bool_user and bool_email:
            user = User.objects.create_user(username=username, email=email, password=password1, first_name=fname, last_name=lname)
            user.is_active = False # kullanıcının giriş yapmasını engelledik
            user.save()

            userinfo = UserInfo(user=user)
            userinfo.save() # save ederken modeldeki save de çalışır emailaktive ve image gönderilir
            
            messages.success(request, "Kaydınız başarıyla tamamlandı emaili doğrulayın...")
            send_mail(
               "Email Doğrulama",
               f"Emaili doğrulamak için linki tıklayın: \n {request.get_host()}/user/email/active/{userinfo.emailactive}",
               EMAIL_HOST_USER,
               [email],
               fail_silently=False,
            )
            
            return redirect("loginUser")
         else:
            return redirect("registerUser")
      
   
   context={}
   return render(request, 'user/register.html', context)


def emailAktive(request, active):

   if UserInfo.objects.filter(emailactive=active).exists():
      userinfo = UserInfo.objects.get(emailactive=active) # yoksa hata verir
      
      userinfo.user.is_active = True
      userinfo.user.save()
      messages.success(request, "Email doğrulamanız yapıldı. Giriş yapabilirsiniz.")
   else:
      messages.error(request, "Yanlış url bağlantısı !")
   
   context = {}
   return redirect("loginUser")
