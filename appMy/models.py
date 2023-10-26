from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Brand(models.Model):
   title = models.CharField(("Marka Başlık"), max_length=50)
   slug = models.SlugField(("Slug"), blank=True, unique=True)
   
   def save(self):
      self.slug = slugify(self.title)
      super().save()
      
   def __str__(self) -> str:
      return self.title

class Category(models.Model):
   title = models.CharField(("Kategori Başlık"), max_length=50)
   slug = models.SlugField(("Slug"), blank=True, unique=True)
   
   def save(self):
      self.slug = slugify(self.title)
      super().save()

   def __str__(self) -> str:
      return self.title

class Color(models.Model):
   title = models.CharField(("Renk Başlık"), max_length=50)
   slug = models.SlugField(("Slug"), blank=True, unique=True)

   def save(self):
      self.slug = slugify(self.title)
      super().save()

   def __str__(self) -> str:
      return self.title



class ProductMain(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   brand = models.ForeignKey(Brand, verbose_name=("Marka"), on_delete=models.CASCADE)
   category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
   title = models.CharField(("Başlık"), max_length=50)
   Description = models.TextField(("Açıklama"))
   comments = models.IntegerField(("Yorum Sayısı"), default=0)
   price = models.FloatField(("Fiyat"))
   slug = models.SlugField(("Slug"), blank=True, unique=True, null=True)

   def __str__(self) -> str:
      return self.title

   def save(self):
      self.slug = slugify(self.title)
      super().save()


class ProductInfo(models.Model):
   CHOICES = [
      ("small", "S"),
      ("medium", "M"),
      ("large", "L"),
      ("xlarge", "XL"),
   ]
   product = models.ForeignKey(ProductMain, verbose_name=("Ürün"), on_delete=models.CASCADE)
   size = models.CharField(("Beden"), choices=CHOICES, max_length=50)
   color = models.ForeignKey(Color, verbose_name=("Renk"), on_delete=models.CASCADE)
   stok = models.IntegerField(("Stok"), default=0)

   def __str__(self) -> str:
      return self.product.title
   

class Image(models.Model):
   product = models.ForeignKey(ProductMain, verbose_name=("Ürün"), on_delete=models.CASCADE)
   image = models.ImageField(("Resim"), upload_to="product", max_length=400)

   def __str__(self) -> str:
      return self.product.title


