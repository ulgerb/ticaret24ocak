from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Brand(models.Model):
   title = models.CharField(("Marka Başlık"), max_length=50)
   slug = models.SlugField(("Slug"), blank=True)
   
   def save(self):
      self.slug = slugify(self.title) # boşluk yerine - , türkçe karakteri ingilizceye dönüştür
      super().save()
      
   def __str__(self) -> str:
      return self.title

class Category(models.Model):
   title = models.CharField(("Kategori Başlık"), max_length=50)
   slug = models.SlugField(("Slug"), blank=True)
   
   def save(self):
      self.slug = slugify(self.title)
      super().save()

   def __str__(self) -> str:
      return self.title

class Color(models.Model):
   title = models.CharField(("Renk Başlık"), max_length=50)
   color_cod = models.CharField(("Renk Kodu"), max_length=50, null=True)
   slug = models.SlugField(("Slug"), blank=True)

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
   slug = models.SlugField(("Slug"), blank=True, null=True)
   image = models.ImageField(("Ürün Kart Resmi"), upload_to="product", max_length=350, null=True)
   rating = models.FloatField(("Ürün Puanı"), default=0)
   
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
      return self.product.title + " " + self.size + " " + self.color.title
   

class Image(models.Model):
   product = models.ForeignKey(ProductMain, verbose_name=("Ürün"), on_delete=models.CASCADE, null=True, related_name='product')
   image = models.ImageField(("Resim"), upload_to="product", max_length=400)

   def __str__(self) -> str:
      return self.product.title



class Comment(models.Model):
   product = models.ForeignKey(ProductMain, verbose_name=("Ürün"), on_delete=models.CASCADE)
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   text = models.TextField(("Yorum"))
   rating = models.IntegerField(("Yorum Puanı"))

   def __str__(self) -> str:
      return self.product.title
   
   
class BasketShop(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   product = models.ForeignKey(ProductInfo, verbose_name=("Ürün"), on_delete=models.CASCADE)
   quanity = models.IntegerField(("Adet"), default=0)
   total_price = models.FloatField(("Toplam Fiyat"), default=0)
   
   def __str__(self) -> str:
      return self.product.product.title + " " + self.product.color.title + " " + self.product.size