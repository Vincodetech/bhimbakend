from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import datetime

class TermsAndConditions(models.Model):
    title = models.CharField(max_length=255, default='')
    # descriptions = models.TextField()
    descriptions = RichTextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.title

class PrivecyAndProlicy(models.Model):
    title = models.CharField(max_length=255, default='')
    descriptions = RichTextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.title

class AboutUsCms(models.Model):
    title1 = models.CharField(max_length=255, default='')
    description1 = RichTextField(blank=True, null=True)
    mission_title = models.CharField(max_length=255, default='', blank=True, null=True)
    mission_description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='cms/', blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.title1

    @staticmethod
    def get_all():
        return AboutUsCms.objects.all()
    

    @staticmethod
    def get_content_by_active():
        return AboutUsCms.objects.get(active=True)

    @staticmethod
    def get_content_by_id(id):
        return AboutUsCms.objects.get(id=id)

class HeaderCms(models.Model):
    image = models.ImageField(upload_to='cms/', blank=True, null=True)
    facebook = models.CharField(max_length=255, default='', blank=True, null=True)
    twitter = models.CharField(max_length=255, default='', blank=True, null=True)
    google = models.CharField(max_length=255, default='', blank=True, null=True)
    instagram = models.CharField(max_length=255, default='', blank=True, null=True)
    youtube = models.CharField(max_length=255, default='', blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return f'{self.facebook}, {self.twitter}, {self.google}, {self.instagram}'

    @staticmethod
    def get_all():
        return HeaderCms.objects.all()
    

    @staticmethod
    def get_content_by_active():
        return HeaderCms.objects.get(active=True)

    @staticmethod
    def get_content_by_id(id):
        return HeaderCms.objects.get(id=id)

class FooterCms(models.Model):
    image = models.ImageField(upload_to='cms/', blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    phone = models.CharField(max_length=255, default='', blank=True, null=True)
    email = models.CharField(max_length=255, default='', blank=True, null=True)
    website = models.CharField(max_length=255, default='', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    copyright_content = models.CharField(max_length=255, default='', blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return f'{self.phone}, {self.email}, {self.website}, {self.copyright_content}'

    @staticmethod
    def get_all():
        return FooterCms.objects.all()
    

    @staticmethod
    def get_content_by_active():
        return FooterCms.objects.get(active=True)

    @staticmethod
    def get_content_by_id(id):
        return FooterCms.objects.get(id=id)

class Inquiry(models.Model):
    name = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='', blank=True, null=True)
    email = models.CharField(max_length=255, default='')
    subject = models.CharField(max_length=255, default='')
    message = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all():
        return Inquiry.objects.all()
    

    @staticmethod
    def get_content_by_active():
        return Inquiry.objects.get(active=True)

    @staticmethod
    def get_content_by_id(id):
        return Inquiry.objects.get(id=id)

class AdminProfile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='admin/', blank=True, null=True)
    phone = models.CharField(max_length=255, default='', blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.phone

class Slider(models.Model):
    image = models.ImageField(upload_to='slider/', blank=True, null=True)
    title = models.CharField(max_length=255, default='', blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.title

class Teacher(models.Model):
    name = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name="Full Name")
    skill = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name="Specialization")
    address = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name="Full Address")
    phone = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name="Phone")
    email = models.CharField(max_length=255, default='', blank=True, null=True, verbose_name="Email")
    discription = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='teacher/', blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.name

class EbookCategory(models.Model):
    category_name = models.CharField(max_length=255, default="")
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.category_name

class Ebook(models.Model):
    title = models.CharField(max_length=255, default="")
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='ebooks/', blank=True, null=True)
    file = models.FileField(upload_to='ebooks/', blank=True, null=True)
    discription = RichTextField(blank=True, null=True)
    category = models.ForeignKey(EbookCategory, on_delete=models.CASCADE, default="", null=True, blank=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.title