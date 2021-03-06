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
from django.http import JsonResponse

def index(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    home_news = News.objects.filter(active=True).order_by('-news_date')[0:4]
    home_blog = Blog.objects.filter(active=True).order_by('-blog_date')[0:4]
    home_ebook = Ebook.objects.filter(active=True)[0:4]
    home_edu = Education.objects.filter(active=True).order_by('-id')[0:3]
    home_teacher = Teacher.objects.filter(active=True).order_by('-id')[0:4]

    total_users = User.objects.filter(is_staff=False).count()
    total_courses = Education.edu_count()
    total_ebooks = Ebook.objects.all().count()
    total_teachers = Teacher.objects.all().count()

    categories = EducationCategory.objects.filter(active=True)

    context = {
        "header_content": header_content,
        "footer_content": footer_content,
        "home_news": home_news,
        "home_blog": home_blog,
        "home_ebook": home_ebook,
        "total_users": total_users,
        "total_courses": total_courses,
        "total_ebooks": total_ebooks,
        "total_teachers": total_teachers,
        "categories": categories,
        "home_edu": home_edu,
        "home_teacher": home_teacher,
    }
    return render(request, 'website/index.html', context)

def load_sub_category(request):
    educatId = request.GET.get('educatId')
    sub_categorylst = EducationSubCategory.objects.filter(category=educatId)
    print("--------------->>>", sub_categorylst)
    return JsonResponse(list(sub_categorylst.values('id', 'category_name')), safe=False)

def load_subjects(request):
    edusubid = request.GET.get('edusubid')
    subjectslst = EduSubjects.objects.filter(sub_category=edusubid)
    print("--------------->>>", subjectslst)
    return JsonResponse(list(subjectslst.values('id', 'subject_name')), safe=False)

def load_chapters(request):
    edusubjectid = request.GET.get('edusubjectid')
    subjectslst = EduChapter.objects.filter(subject=edusubjectid)
    print("--------------->>>", subjectslst)
    return JsonResponse(list(subjectslst.values('id', 'chapter_name')), safe=False)

def aboutus(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    aboutus = AboutUsCms.objects.get(active=True)

    context = {
        "header_content": header_content,
        "footer_content": footer_content,
        "aboutus": aboutus,
    }
    return render(request, 'website/aboutus.html', context)

def courses(request):
    all_edu = None
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    categories = EducationCategory.objects.filter(active=True)

    tagids = request.GET.get("tagids")
    print("=====>>tagids:", tagids)

    if request.method == "POST":
        educate = request.POST.get("category")
        subcategory = request.POST.get("subcategory")
        subject = request.POST.get("subject")
        chapter = request.POST.get("chapter")

        if educate != "0":
            if subcategory != "0":
                if subject != "0":
                    if chapter != "0":
                        all_edu = Education.objects.filter(chapter=chapter, subject=subject, sub_category=subcategory, category=educate)
                        print("=====>BySubject", all_edu)
                    else:
                        all_edu = Education.objects.filter(subject=subject, sub_category=subcategory, category=educate)
                        print("=====>BySubject", all_edu)
                else:
                    all_edu = Education.objects.filter(sub_category=subcategory, category=educate)
                    print("=====>BySubCat", all_edu)
            else:
                all_edu = Education.objects.filter(category=educate)
                print("=====>ByCat", all_edu)
        else:
            all_edu = Education.objects.filter(active=True)
            print("=====>All", all_edu)
    else:
        if tagids:
            all_edu = Education.objects.filter(tags__in=[tagids])
            print("=====>All By Tags", all_edu)
        else:
            all_edu = Education.objects.filter(active=True)
            print("=====>All", all_edu)
    context = {
        "header_content": header_content,
        "footer_content": footer_content,
        "categories": categories,
        "all_edu": all_edu,
    }
    return render(request, 'website/courses.html', context)

def courses_details(request, id):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()

    single_edu = Education.objects.get(id=id)
    related_edu = Education.objects.filter(subject=single_edu.subject.id)
    print("============", related_edu)
    context = {
        "header_content": header_content,
        "footer_content": footer_content,
        "single_edu": single_edu,
        "related_edu": related_edu,
    }
    return render(request, 'website/courses_details.html', context)

def teachers(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    home_teacher = Teacher.objects.filter(active=True)

    context = {
        "header_content": header_content,
        "footer_content": footer_content,
        "home_teacher": home_teacher,
    }
    return render(request, 'website/teachers.html', context)

def teachers_details(request, id):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()

    single_teacher = Teacher.objects.get(id=id)
    related_edu = Education.objects.filter(teacher=id)
    print("============", related_edu)
    context = {
        "header_content": header_content,
        "footer_content": footer_content,
        "single_teacher": single_teacher,
        "related_edu": related_edu,
    }
    return render(request, 'website/teachers_details.html', context)

def news(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    all_news = News.objects.filter(active=True)

    context = {
        "header_content": header_content,
        "footer_content": footer_content,
        "all_news": all_news,
    }
    return render(request, 'website/news.html', context)

def news_details(request, id):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    news = News.objects.get(id=id)
    related_news = News.objects.filter(category=news.category.id)
    context = {
        "header_content": header_content,
        "footer_content": footer_content,
        "news": news,
        "related_news": related_news,
    }
    return render(request, 'website/news_details.html', context)

def blog(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    all_blogs = Blog.objects.filter(active=True)

    context = {
        "header_content": header_content,
        "footer_content": footer_content,
        "all_blogs": all_blogs,
    }
    return render(request, 'website/blog.html', context)

def blog_details(request, id):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    blog = Blog.objects.get(id=id)
    related_blog = Blog.objects.filter(category=blog.category.id)

    context = {
        "header_content": header_content,
        "footer_content": footer_content,
        "blog": blog,
        "related_blog": related_blog,
    }
    return render(request, 'website/blog_details.html', context)

def shop(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    home_ebook = Ebook.objects.filter(active=True)

    context = {
        "header_content": header_content,
        "footer_content": footer_content,
        "home_ebook": home_ebook,
    }
    return render(request, 'website/shop.html', context)

def ebook_details(request, id):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    sigle_ebook = Ebook.objects.get(id=id)
    related_ebook = Ebook.objects.filter(category=sigle_ebook.category.id)

    context = {
        "header_content": header_content,
        "footer_content": footer_content,
        "sigle_ebook": sigle_ebook,
        "related_ebook": related_ebook,
    }
    return render(request, 'website/ebook_details.html', context)

def contactus(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()

    context = {
        "header_content": header_content,
        "footer_content": footer_content,
    }
    return render(request, 'website/contactus.html', context)

def post_contacts(request):
    flag = None
    mgs = None

    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()

    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        contact = Inquiry(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message,
            active=True
        )

        contact.save()
        flag = 'success'
        mgs = 'Thank You For Contact Us.'
        context = {
            "header_content": header_content,
            "footer_content": footer_content,
            "flag": flag,
            "mgs": mgs,
        }
        return render(request, 'website/contactus.html', context)


def register(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            newuser = user_form.save(commit=False)
            newuser.set_password(user_form.cleaned_data['password'])
            newuser.save()
            Profile.objects.create(user=newuser)
            return redirect('login')
        else:
            user_form = UserRegistrationForm()
    else:
        user_form = UserRegistrationForm()
    return render(request, 'website/register.html', {
        'user_form': user_form,
        'header_content': header_content,
        'footer_content': footer_content,
    })

def user_login(request):
    flag = None
    mgs = None

    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()

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
        'header_content': header_content,
        'footer_content': footer_content,
    })

def logout(request):
    request.session.clear()
    return redirect('login')

def edit(request):
    flag = None
    mgs = None
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
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
        'header_content': header_content,
        'footer_content': footer_content,
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
    return render(request, "website/galley.html", {
        'header_content': header_content,
        'footer_content': footer_content,
        'gallery_cat': gallery_cat,
        'images': images,
    })

def terms_conditions_view(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    tc_content = TermsAndConditions.objects.get(active=True)
    return render(request,'website/t_and_c.html', {
        'tc_content': tc_content,
        'header_content': header_content,
        'footer_content': footer_content,
    })

def privecy_policy_view(request):
    header_content = HeaderCms.get_content_by_active()
    footer_content = FooterCms.get_content_by_active()
    pp_content = PrivecyAndProlicy.objects.get(active=True)
    return render(request,'website/privecy_policy.html', {
        'pp_content': pp_content,
        'header_content': header_content,
        'footer_content': footer_content,
    })