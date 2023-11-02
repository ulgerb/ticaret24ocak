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

def detailPage(request,slug, size=None, color=None):

   # product = ProductMain.objects.get(slug=slug)
   if (size is None) and (color is None):
      productinfo = ProductInfo.objects.filter(product__slug=slug).first()
   else:
      productinfo = ProductInfo.objects.get(product__slug=slug, size=size, color=color)
   
   images = Image.objects.filter(product=productinfo.product)
   comments = Comment.objects.filter(product=productinfo.product)
   colors = Color.objects.all()

   productinfo_list = ProductInfo.objects.filter(product__slug=slug).values("color__color_cod").annotate(Count("color"))
   print(productinfo_list)
   
   context = {
      "productinfo": productinfo,
      "comments": comments,
      "images": images,
      "productinfo_list": productinfo_list,
   }
   return render(request, "shop-single.html", context)
