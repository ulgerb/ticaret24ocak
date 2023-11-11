"""
URL configuration for ticaret24ocak project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve 
from django.conf.urls.static import static
from appMy.views import *
from appUser.views import *
from django.conf.urls import handler404, handler500

handler404 = 'appMy.views.error404'
handler500 = 'appMy.views.error500'


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('admin/', admin.site.urls),
    path('', indexPage, name="indexPage"),
    path('about/', aboutPage, name="aboutPage"),
    path('contact/', contactPage, name="contactPage"),
    path('shop/', shopPage, name="shopPage"),
    path('detail/<slug>/', detailPage, name="detailPage1"),
    path('detail/<slug>/<color>/', detailPage, name="detailPage2"),
    path('basketShop/', basketShop, name="basketShop"),
    
    # path('user/', include("appUser.urls"))
    # === USER ===
    path('login/', loginUser, name="loginUser"),
    path('logout/', logoutUser, name="logoutUser"),
    path('register/', registerUser, name="registerUser"),
    path('user/email/active/<active>', emailAktive, name="emailAktive")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
