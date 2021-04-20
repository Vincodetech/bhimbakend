from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from urllib.request import Request, urlopen 
from urllib.parse import quote
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from home.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from home.models import *
from home.forms import *
from myadmin.models import *
from myadmin.forms import *

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

def news_details(request):
    return render(request, 'website/news_details.html')

def blog(request):
    return render(request, 'website/blog.html')

def blog_details(request):
    return render(request, 'website/blog_details.html')

def shop(request):
    return render(request, 'website/shop.html')

def ebook_details(request):
    return render(request, 'website/ebook_details.html')

def contactus(request):
    return render(request, 'website/contactus.html')

def register(request):
    if request.method == 'POST':
        pass
    else:
        user_form = UserRegistrationForm()
    return render(request, 'website/register.html', {
        'user_form': user_form
    })

def user_login(request):
    if request.method == 'POST':
        pass
    else:
        login_form = LoginForm()
    return render(request, 'website/login.html', {
        'login_form': login_form
    })