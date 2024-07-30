from django.shortcuts import render
from .models import News
# Create your views here.
def news(request):
    #  if you want to enable sorting option 
    
    sort=request.GET.get("sort")
    if sort:    
        newss = News.objects.all().order_by(sort) 
    else:
        newss = News.objects.all().order_by("date")
    return render(request,"news.html",context={"newss":newss})
