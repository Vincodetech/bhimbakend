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

def generate_otp():
    rno = random.randrange(1000, 10000)
    return rno

def send_sms(phoneno, otp):
    user = "DEMOUSER"
    key = "1b23df7a0aXX"
    mobile = "+91" + phoneno
    message = "Hi, Your verification code is " + str(otp) + " Please do not share it. www.bhimconnect.com"
    msg = quote(message)
    senderid = "vincod"
    url = f"http://sms.vincode.in/submitsms.jsp?user={user}&key={key}&mobile={mobile}&senderid={senderid}&accusage=1&message={msg}"
    req = Request(url=url, method='GET')
    response = urlopen(req)
    output = response.read() 
    print("=======>>", output)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid:
            newuser = user_form.save(commit=False)
            newuser.set_password(user_form.cleaned_data['password'])
            newuser.save()
            Profile.objects.create(user=newuser)
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'website/register.html', {
        'user_form': user_form
    })

def user_login(request):
    flag = None
    mgs = None
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request,username=cd['username'],
                                      password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    request.session['uid'] = user.id
                    return redirect('index')
                else:
                    flag = 'error'
                    mgs = 'Disabled Account!.'
            else:
                flag = 'error'
                mgs = 'Invalid login Data!.'
    else:
        login_form = LoginForm()
    return render(request, 'website/login.html', {
        'login_form': login_form,
        'flag': flag,
        'msg': mgs,
    })

def logout(request):
    request.session.clear()
    return redirect('login')

def edit(request):
    flag = None
    mgs = None
    user = User.objects.get(id=request.session['uid'])
    user_profile_id = Profile.objects.filter(user=user)
    if not user_profile_id:
        Profile.objects.create(user=user)
    if request.method == 'POST':
        user = User.objects.get(id=request.session['uid'])
        user_form = UserEditForm(request.POST, instance=user)
        profile_form = ProfileEditForm(request.POST, files=request.FILES, instance=user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            flag = 'success'
            mgs = 'Profile Updated Successfully.'
        else:
            flag = 'error'
            mgs = 'Error in Updating your Profile.'
    else:
        user = User.objects.get(id=request.session['uid'])
        user_form = UserEditForm(instance=user)
        profile_form = ProfileEditForm(instance=user.profile)
    user_profile_data = Profile.objects.get(user=user)
    return render(request,'website/edit_user_profile.html',{
        'user_form':user_form,
        'profile_form':profile_form,
        'user_profile_data': user_profile_data,
        'flag': flag,
        'msg': mgs,
    })