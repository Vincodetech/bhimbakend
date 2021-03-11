from django.urls import path, include
from .views import home_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_view.index, name="index"),
    path('register/',home_view.register,name='register'),
    path('login/',home_view.user_login, name='login'),
    path('logout/',home_view.logout_view, name='logout'),
    path('edit/',home_view.edit,name='edit'),
    path('about/',home_view.about,name='about'),
    path('blogview/',home_view.blog,name='blogview'),
    path('blogsingle/<int:id>',home_view.blog_detail,name='blogsingle'),
    path('events/',home_view.events,name='events'),
    path('newsview/',home_view.news,name='newsview'),
    path('newssingle/<int:id>',home_view.news_detail,name='newssingle'),
    path('galleryview/',home_view.gallery,name='galleryview'),
    path('contact/',home_view.contactus,name='contact'),
    path('tc/',home_view.terms_conditions_view,name='tc'),
    path('privecy/',home_view.privecy_policy_view,name='privecy'),
    path('otp/',home_view.otp,name='otp'),
]