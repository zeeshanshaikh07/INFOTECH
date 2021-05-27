from django.shortcuts import render
from main.models import *
# Create your views here.
def home(request):
    news1 = News.objects.all().order_by('-nId')[:3]
    news2 = News.objects.all().order_by('-nId')[3:9]
    blog1 = Blogs.objects.all()[:3]
    return render(request, 'home.html', {'news':news1,'news2':news2, 'blogs':blog1})

def news(request):
    news=News.objects.all().order_by('-nId')
    return render(request, 'news.html', {'news':news})

def about(request):
    return render(request, 'about.html')

def blogs(request):
    blogs=Blogs.objects.all().order_by('-bId')
    return render(request, 'blogs.html',{'blogs':blogs})