from django.shortcuts import render
from .models import *
from django.db.models import Count


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
   colors = Color.objects.all()

   productinfo_list = ProductInfo.objects.filter(product__slug=slug).values("color__color_cod","color__slug", ).annotate(Count("color"))
   productinfo_size = ProductInfo.objects.filter(product__slug=slug, color__slug=color).values("size")
   productinfo_size2 = []
   for i in productinfo_size:
      productinfo_size2.append(i.get("size"))
   size_list = [("small","S"), ("medium","M"),("large","L"), ("xlarge","XL")]
   
   if request.method == "POST":
      submit = request.POST.get("submit")
      if submit == "shopAddSubmit":
         size = request.POST.get("size")
         quanity = request.POST.get("quanity")
         productinfo_detail = ProductInfo.objects.get(product__slug=slug, color__slug=color, size=size)
         
   
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
