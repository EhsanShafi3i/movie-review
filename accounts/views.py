from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm,PassChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


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

@login_required
def logoutaccount(request):
    logout(request)
    return redirect("home")


def loginaccount(request):
    if request.method == "GET":
        return render(request, "loginaccount.html", {'form': AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "loginaccount.html", context={"form": AuthenticationForm, "error": "username and password do not match'})"})
        else:
            login(request, user)
            return redirect("home")

@login_required
def changepassword(request):
        if request.method == 'POST':
            form = PassChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  
                messages.success(request, 'Your password was successfully updated!')
                return redirect('change_password')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PassChangeForm(request.user)
        return render(request, 'changepassword.html', {
            'form': form
        })