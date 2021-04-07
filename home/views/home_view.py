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
from home.models import GalleryCategory
from home.models import Gallery
from home.models import *
from myadmin.models import TermsAndConditions
from myadmin.models import PrivecyAndProlicy
from myadmin.models import AboutUsCms
from myadmin.models import HeaderCms
from myadmin.models import FooterCms
from myadmin.models import Inquiry
from myadmin.models import Slider
from myadmin.forms import InquiryForm
import random
from urllib.request import Request, urlopen 
from urllib.parse import quote
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from home.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

def index(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    slider_images = Slider.objects.filter(active=True)[0:3]
    news = News.objects.filter(active=True).order_by('-created_at')[0:4]
    result = Blog.objects.filter(active=True).order_by('-created_at')[0:4]
    return render(request, "home/index.html", {
        'header_content': header_content,
        'footer_content': footer_content,
        'slider_images': slider_images,
        'news': news,
        'result': result    
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
    id = request.GET.get('id')
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    if not id:
        all_blogs = Blog.get_blog_by_active()
    else:
        all_blogs = Blog.objects.filter(category=id)
    page = request.GET.get('page', 1)
    paginator = Paginator(all_blogs, 8)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    
    return render(request, "home/blog.html", {
        'header_content': header_content,
        'footer_content': footer_content,
        'result': result
    })

def blog_detail(request, id):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    blog_all_categories = BlogCategory.get_category_by_active()
    single_blog = Blog.get_blog_by_id(id)
    all_blogs = Blog.objects.filter(category=single_blog.category)
    page = request.GET.get('page', 1)
    paginator = Paginator(all_blogs, 8)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    data = {
        'result': result,
    }
    return render(request, "home/blog_detail.html", {
        'header_content': header_content,
        'footer_content': footer_content,
        'single_blog': single_blog,
        'blog_all_categories': blog_all_categories,
        'result': result
    })

def events(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    return render(request, "home/events.html", {
        'header_content': header_content,
        'footer_content': footer_content
    })

def news(request):
    id = request.GET.get('id')
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    news_all_categories = NewsCategory.get_category_by_active()
    if not id:
        allnews = News.get_news_by_active()
    else:
        allnews = News.objects.filter(category=id)
    return render(request, "home/news.html", {
        'header_content': header_content,
        'footer_content': footer_content,
        'news_all_categories': news_all_categories,
        'allnews': allnews
    })

def news_detail(request, id):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    news_all_categories = NewsCategory.get_category_by_active()
    single_news = News.get_news_by_id(id)
    allnews = News.objects.filter(category=single_news.category)
    return render(request, "home/news_detail.html", {
        'header_content': header_content,
        'footer_content': footer_content,
        'single_news': single_news,
        'news_all_categories': news_all_categories,
        'allnews': allnews
    })

def gallery(request):
    id = request.GET.get('id')
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    gallery_cat = GalleryCategory.objects.filter(active=True)
    if not id:
        images = Gallery.objects.filter(active=True)
    else:
        images = Gallery.objects.filter(category=id)
    return render(request, "home/galley.html", {
        'header_content': header_content,
        'footer_content': footer_content,
        'gallery_cat': gallery_cat,
        'images': images
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
    return_url = None
    return_url = request.GET.get('return_url')
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    flag = None
    mgs = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = CustomUser.get_user_by_phone(cd['phone'])
            return_url = request.GET.get('return_url')
            if user is not None and user.active:
                request.session['uid'] = user.id
                if return_url:
                    return HttpResponseRedirect(return_url)
                else:
                    return_url = None
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

def edu_cat_list(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    education_all_cat = EducationCategory.get_category_by_active()
    return render(request, 'home/education_category.html', {
       'header_content': header_content, 
       'footer_content': footer_content,
       'education_all_cat': education_all_cat
    })

def edu_sub_cat_list_by_cat(request, id):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    edu_sub_cat_list_for_cat = EducationSubCategory.get_sub_category_by_cat(id)
    page = request.GET.get('page', 1)
    paginator = Paginator(edu_sub_cat_list_for_cat, 4)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    return render(request, 'home/education_sub_category.html', {
       'header_content': header_content, 
       'footer_content': footer_content,
       'result': result
    })

def edu_subjects_list_by_subcat(request, id):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    edu_subjects_list_for_subcat = EduSubjects.get_subjects_by_sub_cat(id)
    page = request.GET.get('page', 1)
    paginator = Paginator(edu_subjects_list_for_subcat, 4)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    return render(request, 'home/education_subjects.html', {
       'header_content': header_content, 
       'footer_content': footer_content,
       'result': result
    })


def edu_chapters_list_by_subjects(request, id):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    edu_chs = Education.objects.filter(subject=id, active=True)
    # page = request.GET.get('page', 1)
    # paginator = Paginator(edu_chs, 4)
    # try:
    #     result = paginator.page(page)
    # except PageNotAnInteger:
    #     result = paginator.page(1)
    # except EmptyPage:
    #     result = paginator.page(paginator.num_pages)
    return render(request, 'home/education_chapters.html', {
       'header_content': header_content, 
       'footer_content': footer_content,
       'result': edu_chs
    })