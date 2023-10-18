
from django.urls import path
from appUser.views import *


urlpatterns = [
    path('login', loginUser, name="loginUser"),
    path('register', registerUser, name="registerUser"),
]
