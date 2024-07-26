from django.urls import path
from .views import *
urlpatterns=[
    path('signupaccount/',signupaccount,name="signupaccount")
]