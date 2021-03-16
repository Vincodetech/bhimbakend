from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from home.models import Country
from home.models import State
from home.models import City
from home.models import Degree
from home.models import CustomUser
from home.models import NewsCategory
from home.models import News
from home.models import Education
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.forms import modelformset_factory
from ..models import *
from ..forms import *
import datetime

def dashboard_admin(request):
    total_users = CustomUser.objects.all().count()
    total_inquiries = Inquiry.objects.all().count()
    total_posts = Blog.blog_count()
    total_news = News.news_count()
    total_materials = Education.edu_count()
    return render(request, 'myadmin/index.html', {
        'total_users': total_users,
        'total_inquiries': total_inquiries,
        'total_posts': total_posts,
        'total_news': total_news,
        'total_materials': total_materials,
    })

def edit_profile(request):
    flag = None
    msg = None
    user = User.objects.get(id=request.user.id)
    user_profile_id = AdminProfile.objects.filter(user=user)
    if not user_profile_id:
        AdminProfile.objects.create(user=user)
    if request.method == 'POST':
        admin_form = AdminEntryEditForm(request.POST, instance=request.user)
        profile_form = AdminProfileEditForm(request.POST, files=request.FILES, instance=request.user.adminprofile)
        
        if admin_form.is_valid() and profile_form.is_valid():
            admin_form.save()
            profile_form.save()
            flag = 'success'
            msg = 'Profile Updated Successfully.'
        else:
            flag = 'error'
            msg = 'Error in Updating your Profile.'
    else:
        admin_form = AdminEntryEditForm(instance=request.user)
        profile_form = AdminProfileEditForm(instance=request.user.adminprofile)
    user_profile_data = AdminProfile.objects.get(user=request.user)
    return render(request, 'myadmin/edit_profile.html', {
        'admin_form': admin_form,
        'profile_form': profile_form,
        'flag': flag,
        'msg': msg,
        'user_profile_data': user_profile_data
    })

def validate(country):
        errMsg = None

        if not country.country_name:
            errMsg = "Category Name is required."

        return errMsg

# crud for Country
def country_view(request):
    allcountries = Country.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(allcountries, 10)
    try:
        countries = paginator.page(page)
    except PageNotAnInteger:
        countries = paginator.page(1)
    except EmptyPage:
        countries = paginator.page(paginator.num_pages)
    data = {
        'countries': countries,
    }
    return render(request, 'myadmin/country_view.html', data)

def post_country(request):
    if request.method == 'POST':
        country_name = request.POST.get('country_name')
        active = request.POST.get('active')

        msg = None

        country = Country(
            country_name=country_name,
            active=True if active == 'True' else False
        )
        
        msg = validate(country)

        values = {
            'name': country_name
        }

        if not msg:
            country.save()
            messages.success(request, 'Country created successfully.')
            return redirect('addcountry')
        else:
            data = {
                'msg': msg,
                'values': values
            }    
            return render(request, 'myadmin/add_country_view.html', data)
    return render(request, 'myadmin/add_country_view.html')

def edit_country(request, id):
    single_country = Country.objects.get(id=id)
    if request.method == 'POST':
        country_name = request.POST.get('country_name')
        active = request.POST.get('active')

        country = Country.objects.get(id=id)
        country.country_name = country_name
        country.active = True if active == 'True' else False
        country.updated_at = datetime.datetime.now()

        country.save()
        messages.success(request, 'Country Updated.')
        return redirect('country')
    return render(request, 'myadmin/edit_country_view.html', {
        'single_country': single_country
    })

def delete_country(request, id):
    country = Country.objects.get(id=id)
    country.delete()
    messages.success(request, 'Country is deleted.')
    return redirect('country')

# crud for state
def state_view(request):
    allstates = State.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(allstates, 10)
    try:
        states = paginator.page(page)
    except PageNotAnInteger:
        states = paginator.page(1)
    except EmptyPage:
        states = paginator.page(paginator.num_pages)
    data = {
        'states': states,
    }
    return render(request, 'myadmin/state_view.html', data)

def post_state(request):
    countries = Country.objects.all()
    if request.method == 'POST':
        state_name = request.POST.get('state_name')
        country = request.POST.get('country')
        country_obj = Country.objects.get(id=country)
        active = request.POST.get('active')

        msg = None

        state = State(
            state_name=state_name,
            country=country_obj,
            active=True if active == 'True' else False
        )

        state.save()
        messages.success(request, 'State created successfully.')
        return redirect('addstate')
    return render(request, 'myadmin/add_state_view.html', {'countries': countries})

def edit_state(request, id):
    single_state = State.objects.get(id=id)
    countries = Country.objects.all()
    if request.method == 'POST':
        state_name = request.POST.get('state_name')
        country = request.POST.get('country_id')
        print("--------------->>country", country)
        country_obj = Country.objects.get(id=country)
        active = request.POST.get('active')

        state = State.objects.get(id=id)
        state.state_name = state_name
        state.country = country_obj
        state.active = True if active == 'True' else False
        state.updated_at = datetime.datetime.now()

        state.save()
        messages.success(request, 'State Updated.')
        return redirect('state')
    return render(request, 'myadmin/edit_state_view.html', {
        'single_state': single_state,
        'countries': countries
    })

def delete_state(request, id):
    state = State.objects.get(id=id)
    state.delete()
    messages.success(request, 'State is deleted.')
    return redirect('state')

# crud for city
def city_view(request):
    allcities = City.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(allcities, 10)
    try:
        cities = paginator.page(page)
    except PageNotAnInteger:
        cities = paginator.page(1)
    except EmptyPage:
        cities = paginator.page(paginator.num_pages)
    data = {
        'cities': cities,
    }
    return render(request, 'myadmin/city_view.html', data)

def post_city(request):
    states = State.objects.all()
    if request.method == 'POST':
        city_name = request.POST.get('city_name')
        state = request.POST.get('state')
        state_obj = State.objects.get(id=state)
        active = request.POST.get('active')

        msg = None

        city = City(
            city_name=city_name,
            state=state_obj,
            active=True if active == 'True' else False
        )

        city.save()
        messages.success(request, 'City created successfully.')
        return redirect('addcity')
    return render(request, 'myadmin/add_city_view.html', {'states': states})

def edit_city(request, id):
    single_city = City.objects.get(id=id)
    states = State.objects.all()
    if request.method == 'POST':
        city_name = request.POST.get('city_name')
        state = request.POST.get('state')
        state_obj = State.objects.get(id=state)
        active = request.POST.get('active')

        city = City.objects.get(id=id)
        city.city_name = city_name
        city.state = state_obj
        city.active = True if active == 'True' else False
        city.updated_at = datetime.datetime.now()

        city.save()
        messages.success(request, 'City Updated.')
        return redirect('city')
    return render(request, 'myadmin/edit_city_view.html', {
        'single_city': single_city,
        'states': states
    })

def delete_city(request, id):
    single_city = City.objects.get(id=id)
    single_city.delete()
    messages.success(request, 'City is deleted.')
    return redirect('city')

# crud for Degree
def degree_view(request):
    alldegree = Degree.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(alldegree, 10)
    try:
        degrees = paginator.page(page)
    except PageNotAnInteger:
        degrees = paginator.page(1)
    except EmptyPage:
        degrees = paginator.page(paginator.num_pages)
    data = {
        'degrees': degrees,
    }
    return render(request, 'myadmin/degree_view.html', data)

def post_degree(request):
    if request.method == 'POST':
        degree_name = request.POST.get('degree_name')
        active = request.POST.get('active')

        degree = Degree(
            degree_name=degree_name,
            active=True if active == 'True' else False
        )
        
        degree.save()
        messages.success(request, 'Degree created successfully.')
        return redirect('adddegree')
    return render(request, 'myadmin/add_degree_view.html')

def edit_degree(request, id):
    single_degree = Degree.objects.get(id=id)
    if request.method == 'POST':
        degree_name = request.POST.get('degree_name')
        active = request.POST.get('active')

        degree = Degree.objects.get(id=id)
        degree.degree_name = degree_name
        degree.active = True if active == 'True' else False
        degree.updated_at = datetime.datetime.now()

        degree.save()
        messages.success(request, 'Degree Updated.')
        return redirect('degree')
    return render(request, 'myadmin/edit_degree_view.html', {
        'single_degree': single_degree
    })

def delete_degree(request, id):
    degree = Degree.objects.get(id=id)
    degree.delete()
    messages.success(request, 'Degree is deleted.')
    return redirect('degree')


def cms_tc(request):
    alldata = TermsAndConditions.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(alldata, 2)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    return render(request, 'myadmin/terms_conditions_view.html', {
        'result': result
    })

def add_tc(request):
    if request.method == 'POST':
        forms = TermsConditionForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Terms & Conditions created successfully.')
            return redirect('addtc')
        else:
            messages.error(request, 'Terms & Conditions is not created successfully.')
            return redirect('addtc')
    else:
        forms = TermsConditionForm()
    return render(request, 'myadmin/add_terms_conditions_view.html', {
        'forms': forms
    })

def edit_tc(request, id):
    tc_content = TermsAndConditions.objects.get(id=id)
    if request.method == 'POST':
        # content = TermsAndConditions.objects.get(id=id)
        forms = TermsConditionForm(request.POST, instance=tc_content)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Terms & Conditions updated successfully.')
            return redirect('admintc')
        else:
            messages.error(request, 'Terms & Conditions is not updated successfully.')
            return redirect('admintc')
    else:
        forms = TermsConditionForm(instance=tc_content)
    return render(request, 'myadmin/add_terms_conditions_view.html', {
        'forms': forms
    })

def delete_tc(request, id):
    tc_content = TermsAndConditions.objects.get(id=id)
    tc_content.delete()
    messages.success(request, 'Terms & Conditions is deleted.')
    return redirect('admintc')

def cms_privacy(request):
    pp_content = PrivecyAndProlicy.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(pp_content, 2)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    return render(request, 'myadmin/privacy_policy_view.html', {
        'result': result
    })

def add_policy(request):
    if request.method == 'POST':
        forms = PrivecyPolicyForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Privecy Policy created successfully.')
            return redirect('addpolicy')
        else:
            messages.error(request, 'Privecy Policy is not created successfully.')
            return redirect('addpolicy')
    else:
        forms = PrivecyPolicyForm()
    return render(request, 'myadmin/add_pp_view.html', {
        'forms': forms
    })

def edit_policy(request, id):
    tc_content = PrivecyAndProlicy.objects.get(id=id)
    if request.method == 'POST':
        # content = TermsAndConditions.objects.get(id=id)
        forms = PrivecyPolicyForm(request.POST, instance=tc_content)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Privecy Policy updated successfully.')
            return redirect('adminpolicy')
        else:
            messages.error(request, 'Privecy Policy is not updated successfully.')
            return redirect('adminpolicy')
    else:
        forms = PrivecyPolicyForm(instance=tc_content)
    return render(request, 'myadmin/add_pp_view.html', {
        'forms': forms
    })

def delete_policy(request, id):
    tc_content = PrivecyAndProlicy.objects.get(id=id)
    tc_content.delete()
    messages.success(request, 'Privecy Policy is deleted.')
    return redirect('adminpolicy')

def users_view(request):
    allusers = CustomUser.objects.all()
    print("============>>", allusers)
    page = request.GET.get('page', 1)
    paginator = Paginator(allusers, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    data = {
        'users': users,
    }
    return render(request, 'myadmin/users.html', data)

def inquiry_view(request):
    allusers = Inquiry.objects.all()
    print("============>>", allusers)
    page = request.GET.get('page', 1)
    paginator = Paginator(allusers, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    data = {
        'users': users,
    }
    return render(request, 'myadmin/inquiry.html', data)

def admin_view(request):
    allusers = User.objects.filter(is_staff=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(allusers, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    data = {
        'users': users,
    }
    return render(request, 'myadmin/admin.html', data)

def add_admin(request):
    if request.method == 'POST':
        forms = AdminEntryForm(request.POST)
        if forms.is_valid():
            new_user = forms.save(commit=False)
            new_user.set_password(forms.cleaned_data['password'])
            new_user.save()
            AdminProfile.objects.create(user=new_user)
            messages.success(request, 'Admin created successfully.')
            return redirect('addadminentry')
        else:
            messages.error(request, 'Admin is not created successfully.')
            return redirect('addadminentry')
    else:
        forms = AdminEntryForm()
    return render(request, 'myadmin/add_admin_view.html', {
        'forms': forms
    })

def edit_admin(request, id):
    if request.method == 'POST':
        single_user = User.objects.get(id=id)
        forms = AdminEntryForm(request.POST, instance=single_user)
        if forms.is_valid():
            existing_user = forms.save(commit=False)
            existing_user.set_password(forms.cleaned_data['password'])
            existing_user.save()
            messages.success(request, 'Admin updated successfully.')
            return redirect('adminentry')
        else:
            messages.error(request, 'Admin is not updated successfully.')
            return redirect('adminentry')
    else:
        single_user = User.objects.get(id=id)
        forms = AdminEntryForm(instance=single_user)
    return render(request, 'myadmin/add_admin_view.html', {
        'forms': forms
    })

def delete_admin(request, id):
    single_user = User.objects.get(id=id)
    single_user.delete()
    messages.success(request, 'Admin is deleted.')
    return redirect('adminentry')

def aboutus_view(request):
    allcontents = AboutUsCms.get_all()
    page = request.GET.get('page', 1)
    paginator = Paginator(allcontents, 10)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    data = {
        'result': result,
    }
    return render(request, 'myadmin/aboutus.html', data)

def add_aboutus(request):
    if request.method == 'POST':
        forms = AboutUsForm(request.POST, files=request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'About Us created successfully.')
            return redirect('addaboutus')
        else:
            messages.error(request, 'About Us is not created successfully.')
            return redirect('addaboutus')
    else:
        forms = AboutUsForm()
    return render(request, 'myadmin/add_aboutus_view.html', {
        'forms': forms
    })

def edit_aboutus(request, id):
    if request.method == 'POST':
        single_content = AboutUsCms.get_content_by_id(id)
        forms = AboutUsForm(request.POST, files=request.FILES, instance=single_content)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'About Us updated successfully.')
            return redirect('addaboutus')
        else:
            messages.error(request, 'About Us is not updated successfully.')
            return redirect('addaboutus')
    else:
        single_content = AboutUsCms.get_content_by_id(id)
        forms = AboutUsForm(instance=single_content)
    return render(request, 'myadmin/add_aboutus_view.html', {
        'forms': forms
    })

def delete_about(request, id):
    single_content = AboutUsCms.get_content_by_id(id)
    single_content.delete()
    messages.success(request, 'About Us is deleted.')
    return redirect('aboutus')

def header_view(request):
    allcontents = HeaderCms.get_all()
    page = request.GET.get('page', 1)
    paginator = Paginator(allcontents, 10)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    data = {
        'result': result,
    }
    return render(request, 'myadmin/headerview.html', data)

def add_header(request):
    if request.method == 'POST':
        forms = HeaderForm(request.POST, files=request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Header created successfully.')
            return redirect('addheader')
        else:
            messages.error(request, 'Header is not created successfully.')
            return redirect('addheader')
    else:
        forms = HeaderForm()
    return render(request, 'myadmin/add_header_view.html', {
        'forms': forms
    })

def edit_header(request, id):
    if request.method == 'POST':
        single_header = HeaderCms.get_content_by_id(id)
        forms = HeaderForm(request.POST, files=request.FILES, instance=single_header)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Header updated successfully.')
            return redirect('header')
        else:
            messages.error(request, 'Header is not updated successfully.')
            return redirect('header')
    else:
        single_header = HeaderCms.get_content_by_id(id)
        forms = HeaderForm(instance=single_header)
    return render(request, 'myadmin/add_header_view.html', {
        'forms': forms
    })

def delete_header(request, id):
    single_header = HeaderCms.get_content_by_id(id)
    single_header.delete()
    messages.success(request, 'About Us is deleted.')
    return redirect('header')

def footer_view(request):
    allcontents = FooterCms.get_all()
    page = request.GET.get('page', 1)
    paginator = Paginator(allcontents, 10)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    data = {
        'result': result,
    }
    return render(request, 'myadmin/footerview.html', data)

def add_footer(request):
    if request.method == 'POST':
        forms = FooterForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Footer created successfully.')
            return redirect('addfooter')
        else:
            messages.error(request, 'Footer is not created successfully.')
            return redirect('addfooter')
    else:
        forms = FooterForm()
    return render(request, 'myadmin/add_footer_view.html', {
        'forms': forms
    })

def edit_footer(request, id):
    if request.method == 'POST':
        single_footer = FooterCms.get_content_by_id(id)
        forms = FooterForm(request.POST, instance=single_footer)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Footer updated successfully.')
            return redirect('footer')
        else:
            messages.error(request, 'Footer is not updated successfully.')
            return redirect('footer')
    else:
        single_footer = FooterCms.get_content_by_id(id)
        forms = FooterForm(instance=single_footer)
    return render(request, 'myadmin/add_footer_view.html', {
        'forms': forms
    })

def delete_footer(request, id):
    single_footer = FooterCms.get_content_by_id(id)
    single_footer.delete()
    messages.success(request, 'Footer is deleted.')
    return redirect('footer')

def news_category_view(request):
    allcontents = NewsCategory.get_all_categories()
    page = request.GET.get('page', 1)
    paginator = Paginator(allcontents, 10)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    data = {
        'result': result,
    }
    return render(request, 'myadmin/newscategoryview.html', data)

def add_news_category(request):
    if request.method == 'POST':
        forms = NewsCatForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'News Category created successfully.')
            return redirect('addnewscategory')
        else:
            messages.error(request, 'News Category is not created successfully.')
            return redirect('addnewscategory')
    else:
        forms = NewsCatForm()
    return render(request, 'myadmin/add_newscat_view.html', {
        'forms': forms
    })

def edit_news_category(request, id):
    if request.method == 'POST':
        single_news_cat = NewsCategory.get_category_by_id(id)
        forms = NewsCatForm(request.POST, instance=single_news_cat)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'News Category updated successfully.')
            return redirect('newscategory')
        else:
            messages.error(request, 'News Category is not updated successfully.')
            return redirect('newscategory')
    else:
        single_news_cat = NewsCategory.get_category_by_id(id)
        forms = NewsCatForm(instance=single_news_cat)
    return render(request, 'myadmin/add_newscat_view.html', {
        'forms': forms
    })

def delete_news_cat(request, id):
    single_news_cat = NewsCategory.get_category_by_id(id)
    single_news_cat.delete()
    messages.success(request, 'News Category is deleted.')
    return redirect('newscategory')

# news crud
def news_view(request):
    allcontents = News.get_all_news()
    page = request.GET.get('page', 1)
    paginator = Paginator(allcontents, 10)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    data = {
        'result': result,
    }
    return render(request, 'myadmin/newsview.html', data)

def add_news(request):
    if request.method == 'POST':
        forms = NewsForm(request.POST, files=request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'News created successfully.')
            return redirect('addnews')
        else:
            messages.error(request, 'News is not created successfully.')
            return redirect('addnews')
    else:
        forms = NewsForm()
    return render(request, 'myadmin/add_news_view.html', {
        'forms': forms
    })

def edit_news(request, id):
    if request.method == 'POST':
        single_news = News.get_news_by_id(id)
        forms = NewsForm(request.POST, instance=single_news, files=request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'News updated successfully.')
            return redirect('news')
        else:
            messages.error(request, 'News is not updated successfully.')
            return redirect('news')
    else:
        single_news = News.get_news_by_id(id)
        forms = NewsForm(instance=single_news)
    return render(request, 'myadmin/add_news_view.html', {
        'forms': forms
    })

def delete_news(request, id):
    single_news = News.get_news_by_id(id)
    single_news.delete()
    messages.success(request, 'News is deleted.')
    return redirect('news')

# blog category crud
def blog_category_view(request):
    allcontents = BlogCategory.get_all_categories()
    page = request.GET.get('page', 1)
    paginator = Paginator(allcontents, 10)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    data = {
        'result': result,
    }
    return render(request, 'myadmin/blogcategoryview.html', data)

def add_blog_category(request):
    if request.method == 'POST':
        forms = BlogCatForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Blog Category created successfully.')
            return redirect('addnblogcategory')
        else:
            messages.error(request, 'Blog Category is not created successfully.')
            return redirect('addnblogcategory')
    else:
        forms = BlogCatForm()
    return render(request, 'myadmin/add_blogcat_view.html', {
        'forms': forms
    })

def edit_blog_category(request, id):
    if request.method == 'POST':
        single_blog_cat = BlogCategory.get_category_by_id(id)
        forms = BlogCatForm(request.POST, instance=single_blog_cat)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Blog Category updated successfully.')
            return redirect('blogcategory')
        else:
            messages.error(request, 'Blog Category is not updated successfully.')
            return redirect('blogcategory')
    else:
        single_blog_cat = BlogCategory.get_category_by_id(id)
        forms = NewsCatForm(instance=single_blog_cat)
    return render(request, 'myadmin/add_blogcat_view.html', {
        'forms': forms
    })

def delete_blog_cat(request, id):
    single_blog_cat = BlogCategory.get_category_by_id(id)
    single_blog_cat.delete()
    messages.success(request, 'Blog Category is deleted.')
    return redirect('blogcategory')

# blog crud
def blog_view(request):
    allcontents = Blog.get_all_blog()
    page = request.GET.get('page', 1)
    paginator = Paginator(allcontents, 10)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    data = {
        'result': result,
    }
    return render(request, 'myadmin/blogview.html', data)

def add_blog(request):
    if request.method == 'POST':
        forms = BlogForm(request.POST, files=request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Blog created successfully.')
            return redirect('addnblog')
        else:
            messages.error(request, 'Blog is not created successfully.')
            return redirect('addnblog')
    else:
        forms = BlogForm()
    return render(request, 'myadmin/add_blog_view.html', {
        'forms': forms
    })

def edit_blog(request, id):
    if request.method == 'POST':
        single_blog = Blog.get_blog_by_id(id)
        forms = BlogForm(request.POST, instance=single_blog, files=request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Blog updated successfully.')
            return redirect('blog')
        else:
            messages.error(request, 'Blog is not updated successfully.')
            return redirect('blog')
    else:
        single_blog = Blog.get_blog_by_id(id)
        forms = BlogForm(instance=single_blog)
    return render(request, 'myadmin/add_blog_view.html', {
        'forms': forms
    })

def delete_blog(request, id):
    single_blog = Blog.get_blog_by_id(id)
    single_blog.delete()
    messages.success(request, 'Blog is deleted.')
    return redirect('blog')

# edu cat crud
def edu_category_view(request):
    allcontents = EducationCategory.get_all_categories()
    page = request.GET.get('page', 1)
    paginator = Paginator(allcontents, 10)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    data = {
        'result': result,
    }
    return render(request, 'myadmin/educategoryview.html', data)

def add_edu_category(request):
    if request.method == 'POST':
        forms = EduCatForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Edu Category created successfully.')
            return redirect('addneducat')
        else:
            messages.error(request, 'Edu Category is not created successfully.')
            return redirect('addneducat')
    else:
        forms = EduCatForm()
    return render(request, 'myadmin/add_educat_view.html', {
        'forms': forms
    })

def edit_edu_category(request, id):
    if request.method == 'POST':
        single_edu_cat = EducationCategory.get_category_by_id(id)
        forms = EduCatForm(request.POST, instance=single_edu_cat)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Edu Category updated successfully.')
            return redirect('educat')
        else:
            messages.error(request, 'Edu Category is not updated successfully.')
            return redirect('educat')
    else:
        single_edu_cat = EducationCategory.get_category_by_id(id)
        forms = EduCatForm(instance=single_edu_cat)
    return render(request, 'myadmin/add_educat_view.html', {
        'forms': forms
    })

def delete_edu_cat(request, id):
    single_edu_cat = EducationCategory.get_category_by_id(id)
    single_edu_cat.delete()
    messages.success(request, 'Edu Category is deleted.')
    return redirect('educat')

# edu sub cat crud
def edu_sub__category_view(request):
    allcontents = EducationSubCategory.get_all_sub_categories()
    page = request.GET.get('page', 1)
    paginator = Paginator(allcontents, 10)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    data = {
        'result': result,
    }
    return render(request, 'myadmin/edusubcategoryview.html', data)

def add_edu_sub_category(request):
    if request.method == 'POST':
        forms = EduSubCatForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Edu Sub Category created successfully.')
            return redirect('addnedusubcat')
        else:
            messages.error(request, 'Edu Sub Category is not created successfully.')
            return redirect('addnedusubcat')
    else:
        forms = EduSubCatForm()
    return render(request, 'myadmin/add_edusubcat_view.html', {
        'forms': forms
    })

def edit_edu_sub_category(request, id):
    if request.method == 'POST':
        single_edu_sub_cat = EducationSubCategory.get_sub_category_by_id(id)
        forms = EduSubCatForm(request.POST, instance=single_edu_sub_cat)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Edu Sub Category updated successfully.')
            return redirect('edusubcat')
        else:
            messages.error(request, 'Edu Sub Category is not updated successfully.')
            return redirect('edusubcat')
    else:
        single_edu_sub_cat = EducationSubCategory.get_sub_category_by_id(id)
        forms = EduSubCatForm(instance=single_edu_sub_cat)
    return render(request, 'myadmin/add_edusubcat_view.html', {
        'forms': forms
    })

def delete_edu_sub_cat(request, id):
    single_edu_sub_cat = EducationSubCategory.get_sub_category_by_id(id)
    single_edu_sub_cat.delete()
    messages.success(request, 'Edu Sub Category is deleted.')
    return redirect('edusubcat')

# edu subjects crud
def edu_subjects_view(request):
    allcontents = EduSubjects.get_all_subjects()
    page = request.GET.get('page', 1)
    paginator = Paginator(allcontents, 10)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    data = {
        'result': result,
    }
    return render(request, 'myadmin/edusubjectsview.html', data)

def add_edu_subjects(request):
    if request.method == 'POST':
        forms = EduSubjectsForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Edu Subjects created successfully.')
            return redirect('addnedusub')
        else:
            messages.error(request, 'Edu Subjects is not created successfully.')
            return redirect('addnedusub')
    else:
        forms = EduSubjectsForm()
    return render(request, 'myadmin/add_edusub_view.html', {
        'forms': forms
    })

def edit_edu_subjects(request, id):
    if request.method == 'POST':
        single_edu_sub = EduSubjects.get_subject_by_id(id)
        forms = EduSubjectsForm(request.POST, instance=single_edu_sub)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Edu Subjects updated successfully.')
            return redirect('edusub')
        else:
            messages.error(request, 'Edu Subjects is not updated successfully.')
            return redirect('edusub')
    else:
        single_edu_sub = EduSubjects.get_subject_by_id(id)
        forms = EduSubjectsForm(instance=single_edu_sub)
    return render(request, 'myadmin/add_edusub_view.html', {
        'forms': forms
    })

def delete_edu_subject(request, id):
    single_edu_sub = EduSubjects.get_subject_by_id(id)
    single_edu_sub.delete()
    messages.success(request, 'Edu Subjects is deleted.')
    return redirect('edusub')

# edu crud
def edu_view(request):
    allcontents = Education.get_all_edu()
    page = request.GET.get('page', 1)
    paginator = Paginator(allcontents, 10)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    data = {
        'result': result,
    }
    return render(request, 'myadmin/eduview.html', data)

def add_edu(request):
    if request.method == 'POST':
        forms = EduForm(request.POST, files=request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Edu created successfully.')
            return redirect('addnedu')
        else:
            messages.error(request, 'Edu is not created successfully.')
            return redirect('addnedu')
    else:
        forms = EduForm()
    return render(request, 'myadmin/add_edu_view.html', {
        'forms': forms
    })

def edit_edu(request, id):
    if request.method == 'POST':
        single_edu = Education.get_edu_by_id(id)
        forms = EduForm(request.POST, instance=single_edu, files=request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Edu updated successfully.')
            return redirect('edu')
        else:
            messages.error(request, 'Edu is not updated successfully.')
            return redirect('edu')
    else:
        single_edu = Education.get_edu_by_id(id)
        forms = EduForm(instance=single_edu)
    return render(request, 'myadmin/add_edu_view.html', {
        'forms': forms
    })

def delete_edu(request, id):
    single_edu = Education.get_edu_by_id(id)
    single_edu.delete()
    messages.success(request, 'Edu is deleted.')
    return redirect('edu')

# gallery cat crud
def gallery_category_view(request):
    allcontents = GalleryCategory.get_all_categories()
    page = request.GET.get('page', 1)
    paginator = Paginator(allcontents, 10)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    data = {
        'result': result,
    }
    return render(request, 'myadmin/gallery_category_view.html', data)

def add_gallery_category(request):
    if request.method == 'POST':
        forms = GalleryCatForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Gallery Category created successfully.')
            return redirect('addgallerycat')
        else:
            messages.error(request, 'Gallery Category is not created successfully.')
            return redirect('addgallerycat')
    else:
        forms = GalleryCatForm()
    return render(request, 'myadmin/add_gallerycat_view.html', {
        'forms': forms
    })

def edit_gallery_category(request, id):
    if request.method == 'POST':
        single_gallery_cat = GalleryCategory.get_category_by_id(id)
        forms = GalleryCatForm(request.POST, instance=single_gallery_cat)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Gallery Category updated successfully.')
            return redirect('gallerycat')
        else:
            messages.error(request, 'Gallery Category is not updated successfully.')
            return redirect('gallerycat')
    else:
        single_gallery_cat = GalleryCategory.get_category_by_id(id)
        forms = GalleryCatForm(instance=single_gallery_cat)
    return render(request, 'myadmin/add_gallerycat_view.html', {
        'forms': forms
    })

def delete_gallery_cat(request, id):
    single_gallery_cat = GalleryCategory.get_category_by_id(id)
    single_gallery_cat.delete()
    messages.success(request, 'Gallery Category is deleted.')
    return redirect('gallerycat')

# Gallery crud
def gallery_view(request):
    allcontents = Gallery.get_all_gallery()
    page = request.GET.get('page', 1)
    paginator = Paginator(allcontents, 10)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    data = {
        'result': result,
    }
    return render(request, 'myadmin/galleryview.html', data)

def add_gallery(request):
    ImageGalleryFormSet = modelformset_factory(Gallery, form=GalleryForm, extra=5)
    if request.method == 'POST':
        forms = ImageGalleryFormSet(request.POST, files=request.FILES, queryset=Gallery.objects.none())
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Gallery Image created successfully.')
            return redirect('addgallery')
        else:
            messages.error(request, 'Gallery Image is not created successfully.')
            return redirect('addgallery')
    else:
        forms = ImageGalleryFormSet(queryset=Gallery.objects.none())
    return render(request, 'myadmin/add_gallery_view.html', {
        'forms': forms
    })


def delete_gallery(request, id):
    single_gallery = Gallery.get_gallery_by_id(id)
    single_gallery.delete()
    messages.success(request, 'Gallery Image is deleted.')
    return redirect('gallery')

# crud for Slider
def slider_view(request):
    allslider = Slider.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(allslider, 10)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    data = {
        'result': result,
    }
    return render(request, 'myadmin/slider_view.html', data)

def post_slider(request):
    if request.method == 'POST':
        forms = SliderForm(request.POST, files=request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Slider created successfully.')
            return redirect('addslider')
        else:
            messages.error(request, 'Slider is not created successfully.')
            return redirect('addslider')
    else:
        forms = SliderForm()
    return render(request, 'myadmin/add_slider_view.html', {
        'forms': forms
    })

def edit_slider(request, id):
    if request.method == 'POST':
        single_slider = Slider.objects.get(id=id)
        forms = SliderForm(request.POST, instance=single_slider, files=request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Slider updated successfully.')
            return redirect('slider')
        else:
            messages.error(request, 'Slider is not updated successfully.')
            return redirect('slider')
    else:
        single_slider = Slider.objects.get(id=id)
        forms = SliderForm(instance=single_slider)
    return render(request, 'myadmin/add_slider_view.html', {
        'forms': forms
    })

def delete_slider(request, id):
    single_slider = Slider.objects.get(id=id)
    single_slider.delete()
    messages.success(request, 'Slider is deleted.')
    return redirect('slider')