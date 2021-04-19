from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.aboutus, name="about"),
    path('course-list/', views.courses, name="course-list"),
    path('teachers-list/', views.teachers, name="teachers-list"),
    path('news/', views.news, name="news-list"),
]