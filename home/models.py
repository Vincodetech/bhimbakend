from django.db import models
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import datetime
from embed_video.fields import EmbedVideoField

class Country(models.Model):
    country_name = models.CharField(max_length=150, default="")
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now) 

    def __str__(self):
        return self.country_name

class State(models.Model):
    state_name = models.CharField(max_length=150, default="")
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.state_name

class City(models.Model):
    city_name = models.CharField(max_length=150, default="")
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name

class Block(models.Model):
    block_name = models.CharField(max_length=150, default="")
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.block_name

class Village(models.Model):
    village_name = models.CharField(max_length=150, default="")
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)

    def __str__(self):
        return self.village_name

class Degree(models.Model):
    degree_name = models.CharField(max_length=200, default="")
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.degree_name

class CustomUser(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=15, unique=True)
    active = models.BooleanField(default=True)
    joined_date = models.DateTimeField(default=datetime.datetime.today)

    @staticmethod
    def get_user_by_phone(phone):
        try:
            return CustomUser.objects.get(phone=phone)
        except:
            return False

    @staticmethod
    def get_user_by_id(id):
        try:
            return CustomUser.objects.get(id=id)
        except:
            return False

class Profile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]

    PROFESSION_CHOICES = [
        ('Student', 'Student'),
        ('Profession', 'Profession'),
        ('Business', 'Business'),
        ('Government Servant', 'Government Servant'),
        ('Social Worker', 'Social Worker'),
        ('Private Job', 'Private Job')
    ]

    user = models.OneToOneField(CustomUser ,on_delete=models.CASCADE)
    intrests = models.CharField(max_length=255, default="",blank=True, null=True)
    date_of_birth = models.CharField(blank=True,null=True, default="", max_length=255)
    photo = models.ImageField(upload_to='users/', blank=True, null=True)
    gender = models.CharField(max_length=15, default="", choices=GENDER_CHOICES, blank=True, null=True)
    street1 = models.CharField(max_length=200, blank=True, null=True, default="")
    street2 = models.CharField(max_length=200, blank=True, null=True, default="")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default="", blank=True, null=True)
    add_state = models.ForeignKey(State, on_delete=models.CASCADE, default="", blank=True, null=True)
    add_city = models.ForeignKey(City, on_delete=models.CASCADE, default="", blank=True, null=True, verbose_name="Enter District")
    add_block = models.CharField(max_length=255, default="", blank=True, null=True, verbose_name="Enter Taluka")
    add_village = models.CharField(max_length=255, default="", blank=True, null=True, verbose_name="Enter Village")
    add_international = models.TextField(blank=True, null=True, verbose_name="International Address")
    degree = models.CharField(max_length=255, default="", blank=True, null=True, verbose_name="Enter Degree")
    profession_type = models.CharField(max_length=150, default="", blank=True, null=True, choices=PROFESSION_CHOICES)
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Profession Details")
    created_at = models.DateField(default=datetime.datetime.now, blank=True, null=True)
    updated_at = models.DateField(default=datetime.datetime.now, blank=True, null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

class NewsCategory(models.Model):
    category_name = models.CharField(max_length=255, default="")
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.category_name

    @staticmethod
    def get_all_categories():
        return NewsCategory.objects.all()

    @staticmethod
    def get_category_by_id(id):
        return NewsCategory.objects.get(id=id)

    @staticmethod
    def get_category_by_active():
        return NewsCategory.objects.filter(active=True)

class BlogCategory(models.Model):
    category_name = models.CharField(max_length=255, default="")
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)


    def __str__(self):
        return self.category_name


    @staticmethod
    def get_all_categories():
        return BlogCategory.objects.all()

    @staticmethod
    def get_category_by_id(id):
        return BlogCategory.objects.get(id=id)

    @staticmethod
    def get_category_by_active():
        return BlogCategory.objects.filter(active=True)

class News(models.Model):
    title = models.CharField(max_length=255, default="")
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    youtube_link = EmbedVideoField(default="", blank=True, null=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, default="")
    news_date = models.DateField(default=datetime.datetime.now)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.title

    @staticmethod
    def get_all_news():
        return News.objects.all()

    @staticmethod
    def news_count():
        return News.objects.all().count()

    @staticmethod
    def get_news_by_id(id):
        return News.objects.get(id=id)

    @staticmethod
    def get_news_by_active():
        return News.objects.filter(active=True)

class Blog(models.Model):
    title = models.CharField(max_length=255, default="")
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    youtube_link = EmbedVideoField(default="", blank=True, null=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, default="")
    blog_date = models.DateField(default=datetime.datetime.now)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.title

    @staticmethod
    def get_all_blog():
        return Blog.objects.all()
    
    @staticmethod
    def blog_count():
        return Blog.objects.all().count()

    @staticmethod
    def get_blog_by_id(id):
        return Blog.objects.get(id=id)

    @staticmethod
    def get_blog_by_active():
        return Blog.objects.filter(active=True)

class EducationCategory(models.Model):
    category_name = models.CharField(max_length=255, default="")
    photo = models.ImageField(upload_to='educattion/', default="", blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.category_name

    @staticmethod
    def get_all_categories():
        return EducationCategory.objects.all()

    @staticmethod
    def get_category_by_id(id):
        return EducationCategory.objects.get(id=id)

    @staticmethod
    def get_category_by_active():
        return EducationCategory.objects.filter(active=True)

class EducationSubCategory(models.Model):
    category_name = models.CharField(max_length=255, default="")
    image = models.ImageField(upload_to='educattion/', default="",  blank=True, null=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(EducationCategory, on_delete=models.CASCADE, default="")
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.category_name

    @staticmethod
    def get_all_sub_categories():
        return EducationSubCategory.objects.all()

    @staticmethod
    def get_sub_category_by_id(id):
        return EducationSubCategory.objects.get(id=id)

    @staticmethod
    def get_sub_category_by_active():
        return EducationSubCategory.objects.filter(active=True)

    @staticmethod
    def get_sub_category_by_cat(id):
        return EducationSubCategory.objects.filter(category=id)

class EduSubjects(models.Model):
    subject_name = models.CharField(max_length=255, default="")
    image = models.ImageField(upload_to='educattion/', default="", blank=True, null=True)
    active = models.BooleanField(default=True)
    sub_category = models.ForeignKey(EducationSubCategory, on_delete=models.CASCADE, default="")
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.subject_name

    @staticmethod
    def get_all_subjects():
        return EduSubjects.objects.all()

    @staticmethod
    def get_subject_by_id(id):
        return EduSubjects.objects.get(id=id)

    @staticmethod
    def get_subjects_by_active():
        return EduSubjects.objects.filter(active=True)

    @staticmethod
    def get_subjects_by_sub_cat(id):
        return EduSubjects.objects.filter(sub_category=id)

class Education(models.Model):
    title = models.CharField(max_length=255, default="")
    description = RichTextField(blank=True, null=True)
    document_path = models.FileField(upload_to="material/", default="", blank=True, null=True)
    image = models.ImageField(upload_to='educattion/', default="", blank=True, null=True)
    youtube_link = EmbedVideoField(default="", blank=True, null=True)
    youtube_channel_link = models.CharField(max_length=255, default="", blank=True, null=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(EducationCategory, on_delete=models.CASCADE, default="")
    sub_category = models.ForeignKey(EducationSubCategory, on_delete=models.CASCADE, default="")
    subject = models.ForeignKey(EduSubjects, on_delete=models.CASCADE, default="", null=True, blank=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.category_name
        
    @staticmethod
    def get_all_edu():
        return Education.objects.all()

    @staticmethod
    def edu_count():
        return Education.objects.all().count()

    @staticmethod
    def get_edu_by_id(id):
        return Education.objects.get(id=id)

    @staticmethod
    def get_edu_by_active():
        return Education.objects.filter(active=True)

class GalleryCategory(models.Model):
    category_name = models.CharField(max_length=255, default="")
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.category_name

    @staticmethod
    def get_all_categories():
        return GalleryCategory.objects.all()

    @staticmethod
    def get_category_by_id(id):
        return GalleryCategory.objects.get(id=id)

    @staticmethod
    def get_category_by_active():
        return GalleryCategory.objects.filter(active=True)

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, default="")
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.datetime.now)
    updated_at = models.DateField(default=datetime.datetime.now)

    @staticmethod
    def get_all_gallery():
        return Gallery.objects.all()

    @staticmethod
    def get_gallery_by_id(id):
        return Gallery.objects.get(id=id)

    @staticmethod
    def get_gallery_by_active():
        return Gallery.objects.filter(active=True)