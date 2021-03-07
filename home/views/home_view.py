from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from home.forms import UserRegistrationForm, LoginForm, UserEditForm, ProfileEditForm
# from home.forms import WorkEditProfileForm
from home.models import Profile
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from home.models import CustomUser
from django.core.files.storage import FileSystemStorage
from home.models import Country
from home.models import State
from home.models import City
from home.models import Degree
from myadmin.models import TermsAndConditions
from myadmin.models import PrivecyAndProlicy
from myadmin.models import AboutUsCms
from myadmin.models import HeaderCms
from myadmin.models import FooterCms
from myadmin.models import Inquiry
from myadmin.forms import InquiryForm
import random
from urllib.request import Request, urlopen 
from urllib.parse import quote

def index(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    return render(request, "home/index.html", {
        'header_content': header_content,
        'footer_content': footer_content
    })

def about(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    about_content = AboutUsCms.get_content_by_active()
    return render(request, "home/about.html", {
        'about_content': about_content,
        'header_content': header_content,
        'footer_content': footer_content
    })

def blog(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    return render(request, "home/blog.html", {
        'header_content': header_content,
        'footer_content': footer_content
    })

def events(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    return render(request, "home/events.html", {
        'header_content': header_content,
        'footer_content': footer_content
    })

def news(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    return render(request, "home/news.html", {
        'header_content': header_content,
        'footer_content': footer_content
    })

def gallery(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    return render(request, "home/galley.html", {
        'header_content': header_content,
        'footer_content': footer_content
    })

def contactus(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    flag = None
    msg = None
    if request.method == 'POST':
        forms = InquiryForm(request.POST)
        if forms.is_valid():
            forms.save()
            flag = 'success'
            msg = 'Your Message Successfully Sent.'
        else:
            flag = 'error'
            msg = 'Your Message was not Successfully Sent.'
    else:
        forms = InquiryForm()
    return render(request, "home/contactus.html", {
        'header_content': header_content,
        'footer_content': footer_content,
        'forms': forms,
        'flag': flag,
        'msg': msg
    })

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
    flag = None
    msg = None
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            user = CustomUser.get_user_by_phone(cd['phone'])
            if not user:
                new_user = user_form.save(commit=False)
                new_user.save()
                Profile.objects.create(user=new_user)
                otp = generate_otp()
                send_sms(cd['phone'], otp)
                return render(request,'home/otp.html',{
                    'otp': otp,
                    'header_content': header_content,
                    'footer_content': footer_content
                })
            else:
                flag = 'error'
                msg = 'You have already registered with this mobile no. Please enter another phone number.'
        else:
            flag = 'error'
            msg = 'something is wrong.'
    else:
        user_form = UserRegistrationForm()
    return render(request,'home/register.html',{
        'user_form': user_form,
        'header_content': header_content,
        'footer_content': footer_content,
        'flag': flag,
        'msg': msg
    })

def otp(request):
    flag = None
    msg = None
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    if request.method == 'POST':
        otp = request.POST.get('otp')
        gotp = request.POST.get('gotp')
        print("------------>>", gotp, otp)
        if otp == gotp:
            return redirect('login')
        else:
            flag = 'error'
            msg = 'Invalid Otp'
    return render(request,'home/otp.html', {
        'flag': flag,
        'msg': msg,
        'header_content': header_content,
        'footer_content': footer_content
    })

def user_login(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    flag = None
    mgs = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = CustomUser.get_user_by_phone(cd['phone'])
            if user is not None and user.active:
                request.session['uid'] = user.id
                return redirect("index")
            else:
                flag = 'error'
                mgs = 'Disabled Account!.'
        else:
            flag = 'error'
            mgs = 'Invalid login Data!.'
    else:
        form=LoginForm()
    return render(request,'home/login.html',{
        'form':form,
        'flag': flag,
        'msg': mgs,
        'header_content': header_content,
        'footer_content': footer_content
    })

def logout_view(request):
    request.session.clear()
    return redirect('login')


def edit(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    flag = None
    mgs = None
    user = CustomUser.objects.get(id=request.session['uid'])
    user_profile_id = Profile.objects.filter(user=user)
    if not user_profile_id:
        Profile.objects.create(user=user)
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.session['uid'])
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
        user = CustomUser.objects.get(id=request.session['uid'])
        user_form = UserEditForm(instance=user)
        profile_form = ProfileEditForm(instance=user.profile)
    user_profile_data = Profile.objects.get(user=user)
    return render(request,'home/edit.html',{
        'user_form':user_form,
        'profile_form':profile_form,
        'user_profile_data': user_profile_data,
        'flag': flag,
        'msg': mgs,
        'header_content': header_content,
        'footer_content': footer_content
    })

def terms_conditions_view(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    tc_content = TermsAndConditions.objects.get(active=True)
    return render(request,'home/t_and_c.html', {
        'tc_content': tc_content,
        'header_content': header_content,
        'footer_content': footer_content
    })

def privecy_policy_view(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    pp_content = PrivecyAndProlicy.objects.get(active=True)
    return render(request,'home/privecy_policy.html', {
        'pp_content': pp_content,
        'header_content': header_content,
        'footer_content': footer_content
    })