from django import forms
from django.contrib.auth.models import User
from .models import *
from home.models import *
from myadmin.models import *

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
        fields=('category_name', 'photo', 'active')

class EduSubCatForm(forms.ModelForm):
    class Meta:
        model=EducationSubCategory
        fields=('category_name', 'category', 'image', 'active')

class EduSubjectsForm(forms.ModelForm):
    class Meta:
        model=EduSubjects
        fields=('subject_name', 'sub_category', 'image', 'active')

class EduForm(forms.ModelForm):
    class Meta:
        model=Education
        fields=('title','description', 'image','document_path','youtube_link','youtube_channel_link',
        'category','sub_category', 'subject', 'teacher', 'tags', 'active')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub_category'].queryset = EducationSubCategory.objects.none()
        self.fields['subject'].queryset = EduSubjects.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['sub_category'].queryset = EducationSubCategory.objects.filter(category=category_id).order_by('category_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset

        if 'sub_category' in self.data:
            try:
                category_id = int(self.data.get('sub_category'))
                self.fields['subject'].queryset = EduSubjects.objects.filter(sub_category=category_id).order_by('subject_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.id:
            self.fields['category'].queryset = EducationCategory.objects.all()
            self.fields['sub_category'].queryset = EducationSubCategory.objects.filter(category=self.instance.category)
            self.fields['subject'].queryset = EduSubjects.objects.filter(sub_category=self.instance.sub_category)

class DateInput(forms.DateInput):
    input_type = 'date'

class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields=('title','description','image','youtube_link','category', 'news_date','active')
        widgets = {
            'news_date': DateInput()
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title','description','image','youtube_link','category', 'blog_date','active')
        widgets = {
            'blog_date': DateInput()
        }

class GalleryCatForm(forms.ModelForm):
    class Meta:
        model=GalleryCategory
        fields=('category_name', 'active')

class GalleryForm(forms.ModelForm):
    class Meta:
        model=Gallery
        fields=('image','category','active')

class SliderForm(forms.ModelForm):
    class Meta:
        model=Slider
        fields=('title', 'image', 'active')

class TeachererForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=('name','skill','address','phone','email','discription','image','active')

class TagForm(forms.ModelForm):
    class Meta:
        model=Tag
        fields=('__all__')

class EbookCatForm(forms.ModelForm):
    class Meta:
        model=EbookCategory
        fields=('category_name', 'active')

class EbookForm(forms.ModelForm):
    class Meta:
        model=Ebook
        fields=('title','discription','image','file','category','active')