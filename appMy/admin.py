from django.contrib import admin
from .models import *


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
   list_display = ('title',)
   readonly_fields = ('slug',)
   
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('title',)
   readonly_fields = ('slug',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
   list_display = ('title',)
   readonly_fields = ('slug',)
   
@admin.register(ProductMain)
class ProductMainAdmin(admin.ModelAdmin):
   list_display = ('title','brand', 'category', 'price')
   readonly_fields = ('slug',)
   search_fields = ('title', 'brand', 'category')


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
   list_display = ('product', 'size', 'color', 'stok')
   search_fields = ('product', 'size', 'color')

@admin.register(BasketShop)
class BasketShopAdmin(admin.ModelAdmin):
   list_display = ('user','product','productSize','productColor','quanity','total_price')
   search_fields = ('product',"user")

   def productSize(self,obj):
      return obj.product.size
   
   def productColor(self, obj):
      return obj.product.color.title      

admin.site.register(Image)