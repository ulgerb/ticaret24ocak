from django.shortcuts import render,redirect
from .models import *
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def indexPage(request):
   context = {}
   return render(request, "index.html", context)

def aboutPage(request):
   context = {}
   return render(request, "about.html", context)

def contactPage(request):
   context = {}
   return render(request, "contact.html", context)

def shopPage(request): 
   product_list = ProductMain.objects.all().order_by("-id")
   context = {
      "product_list":product_list,
   }
   return render(request, "shop.html", context)

def detailPage(request,slug, color=None):

   # product = ProductMain.objects.get(slug=slug)
   if color is None:
      productinfo = ProductInfo.objects.filter(product__slug=slug).first()
      color = productinfo.color.slug
   else:
      productinfo = ProductInfo.objects.filter(product__slug=slug, color__slug=color).first()
      
   color_cod = productinfo.color.color_cod
   
   images = Image.objects.filter(product=productinfo.product)
   comments = Comment.objects.filter(product=productinfo.product)

   productinfo_list = ProductInfo.objects.filter(product__slug=slug).values("color__color_cod","color__slug", ).annotate(Count("color"))
   productinfo_size = ProductInfo.objects.filter(product__slug=slug, color__slug=color).values("size")
   productinfo_size2 = []
   for i in productinfo_size:
      productinfo_size2.append(i.get("size"))
   size_list = [("small","S"), ("medium","M"),("large","L"), ("xlarge","XL")]
   
   if request.user.is_authenticated:
      if request.method == "POST":
         submit = request.POST.get("submit")
         if submit == "shopAddSubmit":
            size = request.POST.get("size")
            quanity = request.POST.get("quanity")
            if size and quanity:
               productinfo_detail = ProductInfo.objects.filter(product__slug=slug, color__slug=color, size=size).first()
               
               # ürün sepette hiç yoksa yeni obj oluştur. varsa bu objenin adetini güncelle
               if not BasketShop.objects.filter(product=productinfo_detail, user=request.user).exists():
                  basketshop = BasketShop(user=request.user,quanity=quanity, product=productinfo_detail )
                  basketshop.total_price = float(basketshop.product.product.price) * int(basketshop.quanity)
                  basketshop.save()
               else:
                  basketshop = BasketShop.objects.filter(product=productinfo_detail, user=request.user).first()
                  basketshop.quanity = int(basketshop.quanity) + int(quanity)
                  basketshop.total_price = float(basketshop.product.product.price) * int(basketshop.quanity)
                  basketshop.save()
               
            return redirect("detailPage2", slug=slug, color=color)
   else:
      messages.error(request, "Ürünü satın alabilmek için giriş yapınız!")
      return redirect("loginPage")
   
   context = {
      "productinfo": productinfo,
      "comments": comments,
      "images": images,
      "productinfo_list": productinfo_list,
      "productinfo_size2": productinfo_size2,
      "color_cod": color_cod,
      "size_list": size_list,
   }
   return render(request, "shop-single.html", context)

@login_required(login_url="loginUser")
def basketShop(request):
   basket = BasketShop.objects.filter(user=request.user)
   total = 0
   for i in basket:
      total += i.total_price
   
   context = {
      "basket":basket,
      "total":total,
   }
   return render(request, "user/basketshop.html", context)




# ERROR 404 500
def error404(request,exception):
   return render(request,"error/404.html")

def error500(request):
   return render(request,"error/500.html")