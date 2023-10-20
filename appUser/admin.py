from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class UserInfoInline(admin.StackedInline):
   model = UserInfo
   max_num = 1
   can_delete = False
   
class CustomUser(UserAdmin):
   inlines = (UserInfoInline,)
   
admin.site.unregister(User)
admin.site.register(User,CustomUser)
  

