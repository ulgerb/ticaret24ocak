from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

class UserInfo(models.Model):
   CHOICES = [
      ("yetkili","yetkili"),
      ("satici", "satici"),
      ("normal","normal"),
   ]
   user = models.OneToOneField(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   image = models.ImageField(("Profile"), upload_to="user", max_length=300, null=True, blank=True)
   address = models.TextField(("Kullanıcı Adresi"), default="", blank=True)
   group = models.CharField(("Kullanıcı Sınıfı"), choices=CHOICES,max_length=50, default="normal")
   emailactive = models.CharField(("Email Active"), max_length=100, null=True, blank=True)
   
   def __str__(self):
      return self.user.username
   
   def save(self):
      if not self.image:
         self.image = "default/user.png"
      
      if self.emailactive is None:
         users = UserInfo.objects.all().values("emailactive")
         # self.emailactive = get_random_string(length=64)
         
         while True:
            randomemail = get_random_string(length=64)
            for i in users:
               if i["emailactive"] == randomemail:
                  break
            else:
               self.emailactive = randomemail
               break
      super().save()
            
            
      
   
   

