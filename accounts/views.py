from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.db import IntegrityError


def signupaccount(request):
    if request.method == "GET":
        return render(request, "signupaccount.html", {"form": UserCreateForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                return render(request, "signupaccount.html", context={"form": UserCreateForm(), "error": "Username already taken. Choose new username"})
        else:
            return render(request, "signupaccount.html", context={"form": UserCreateForm(), "error": "Passwords do not match"})


def logoutaccount(request):
    logout(request)
    return redirect("home")
