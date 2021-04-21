from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.aboutus, name="about"),
    path('course-list/', views.courses, name="course-list"),
    path('teachers-list/', views.teachers, name="teachers-list"),
    path('news/', views.news, name="news-list"),
    path('singlenews/', views.news_details, name="news-detail"), #panding
    path('blog/', views.blog, name="blog-list"),
    path('singleblog/', views.blog_details, name="blog-detail"), #panding
    path('ebooks/', views.shop, name="ebooks-list"),
    path('singleebook/', views.ebook_details, name="ebooks-detail"), #panding
    path('contact/', views.contactus, name="contact"),

    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.edit,name='user-profile'),

    path('tc/',views.edit,name='tc'),
    path('privecy/',views.edit,name='privecy'),
]