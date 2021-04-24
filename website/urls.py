from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.aboutus, name="about"),
    path('course-list/', views.courses, name="course-list"),
    path('course-details/<int:id>', views.courses_details, name="course-details"),
    path('teachers-list/', views.teachers, name="teachers-list"),
    path('teachers-details/<int:id>', views.teachers_details, name="teachers-details"),
    path('news/', views.news, name="news-list"),
    path('singlenews/<int:id>', views.news_details, name="news-detail"), #panding
    path('blog/', views.blog, name="blog-list"),
    path('singleblog/<int:id>', views.blog_details, name="blog-detail"), #panding
    path('ebooks/', views.shop, name="ebooks-list"),
    path('singleebook/<int:id>', views.ebook_details, name="ebooks-detail"),
    path('contact/', views.contactus, name="contact"),
    path('post-contact/', views.post_contacts, name="post-contact"),

    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.edit,name='user-profile'),

    path('tc/',views.edit,name='tc'),
    path('privecy/',views.edit,name='privecy'),

    path('edcat/',views.load_sub_category,name='edcat-ajax'),
    path('sub/',views.load_subjects,name='sub-ajax'),

    path('gallery/',views.gallery,name='gallery-view'),
]