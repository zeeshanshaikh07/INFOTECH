from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def news(request):
    return render(request, 'news.html')

def about(request):
    return render(request, 'about.html')

def blogs(request):
    return render(request, 'blogs.html')