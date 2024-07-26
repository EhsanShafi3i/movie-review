from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def signupaccount(request):
    return render(request, "signupaccount.html", {"form": UserCreationForm})
