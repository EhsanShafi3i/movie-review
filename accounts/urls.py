from django.urls import path
from .views import *

urlpatterns = [
    path('signupaccount/', signupaccount, name="signupaccount"),
    path('logout/', logoutaccount, name='logoutaccount'),
    path("login/", loginaccount, name='loginaccount'),
    path("changepassword",changepassword,name="changepassword")
]
