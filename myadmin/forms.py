from django import forms
from django.contrib.auth.models import User
from .models import *
from home.models import *

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class TermsConditionForm(forms.ModelForm):
    class Meta:
        model=TermsAndConditions
        fields=('title', 'descriptions', 'active')

class PrivecyPolicyForm(forms.ModelForm):
    class Meta:
        model=PrivecyAndProlicy
        fields=('title', 'descriptions', 'active')

class AdminEntryForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('email','username','password','is_staff','is_active')

class AboutUsForm(forms.ModelForm):
    class Meta:
        model=AboutUsCms
        fields=('title1', 'description1','mission_title', 'mission_description','image', 'active')

class HeaderForm(forms.ModelForm):
    class Meta:
        model=HeaderCms
        fields=('image', 'facebook', 'twitter', 'google', 'instagram', 'youtube', 'active')

class FooterForm(forms.ModelForm):
    class Meta:
        model=FooterCms
        fields=('description', 'phone', 'email', 'website', 'copyright_content', 'address', 'active')

class InquiryForm(forms.ModelForm):
    class Meta:
        model=Inquiry
        fields=('name', 'email', 'subject', 'phone', 'message')

class AdminEntryEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email', 'username')

class AdminProfileEditForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = ('photo','phone')

class NewsCatForm(forms.ModelForm):
    class Meta:
        model=NewsCategory
        fields=('category_name', 'active')

class BlogCatForm(forms.ModelForm):
    class Meta:
        model=BlogCategory
        fields=('category_name', 'active')

class EduCatForm(forms.ModelForm):
    class Meta:
        model=EducationCategory
        fields=('category_name', 'active')

class EduSubCatForm(forms.ModelForm):
    class Meta:
        model=EducationSubCategory
        fields=('category_name', 'category', 'active')

class EduSubjectsForm(forms.ModelForm):
    class Meta:
        model=EduSubjects
        fields=('subject_name', 'sub_category', 'active')

class EduForm(forms.ModelForm):
    class Meta:
        model=Education
        fields=('title','description','document_path','youtube_link','youtube_channel_link','category','sub_category', 'subject', 'active')

class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields=('title','description','image','youtube_link','category','active')

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title','description','image','youtube_link','category','active')

class GalleryCatForm(forms.ModelForm):
    class Meta:
        model=GalleryCategory
        fields=('category_name', 'active')

class GalleryForm(forms.ModelForm):
    class Meta:
        model=Gallery
        fields=('image','category','active')