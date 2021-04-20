from django import forms
from .models import CustomUser
from .models import Profile
from django.conf import settings
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username=forms.CharField(label='User Name OR Email')
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ('username')

class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repeat Password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ('first_name', 'last_name', 'email','username')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email', 'phone')

class DateInput(forms.DateInput):
    input_type = 'date'

class RadioSelect(forms.RadioSelect):
    input_type = "radio"

INTREST_CHOICES = [
    ('News', 'News'),
    ('Sports', 'Sports'),
    ('Entertainment', 'Entertainment'),
    ('Politics', 'Politics'),
    ('Business', 'Business'),
    ('Education', 'Education')
]

class ProfileEditForm(forms.ModelForm):
    intrests = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=INTREST_CHOICES)
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'gender','photo', 'street1', 'street2','country','add_state','add_city',
                    'add_block','add_village','add_international','degree','profession_type','title', 'intrests')
        widgets = {
            'date_of_birth': DateInput(),
            'gender': RadioSelect(),
        }