from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect




def home(request):
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html',{'searchTerm':searchTerm})


def about(request):
    return HttpResponse("<h1>welcome to About page</h1>")

def signup(request):
    email = request.GET.get("email")
    return render(request,'signup.html',{"email":email})