from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'website/index.html')

def aboutus(request):
    return render(request, 'website/aboutus.html')

def courses(request):
    return render(request, 'website/courses.html')

def teachers(request):
    return render(request, 'website/teachers.html')

def news(request):
    return render(request, 'website/news.html')