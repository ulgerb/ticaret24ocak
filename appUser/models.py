from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
   CHOICES = [
      ("yetkili","yetkili"),
      ("satici", "satici"),
      ("normal","normal"),
   ]
   user = models.OneToOneField(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   image = models.ImageField(("Profile"), upload_to="user", max_length=300, default="default/user.png")
   address = models.TextField(("Kullanıcı Adresi"), default="", blank=True)
   group = models.CharField(("Kullanıcı Sınıfı"), choices=CHOICES,max_length=50, default="normal")

   
   def __str__(self):
      return self.user.username
   
   

