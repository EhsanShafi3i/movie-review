from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Movie



def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(item_icontains=searchTerm)
    else:
        movies = movies.objects.all()
    return render(request,'.home.html',context={"searchTerm":searchTerm,'movies':movies})
def about(request):
    return HttpResponse("<h1>welcome to About page</h1>")

def signup(request):
    email = request.GET.get("email")
    return render(request,'signup.html',{"email":email})