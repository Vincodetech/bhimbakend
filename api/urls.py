from django.urls import path
from .views import *

urlpatterns = [
    path('register', perform_registration, name="registerapi"),
    path('login', perform_login, name="loginapi"),
    path('profile/<int:id>', user_profile, name="profileapi"),
    path('updateprofile/<int:id>', updateUserProfile, name="updateprofileapi"),
    path('user/<int:id>', get_user, name="userapi"),

    path('countrylist', country_list, name="countrylist"),
    path('statelist', state_list, name="statelist"),
    path('citylist', city_list, name="citylist"),

    path('educatlistlist', education_category_list, name="educatlistlist"),
    path('educat/<int:id>', education_category, name="educat"),

    path('edusubcatlistlist', education_sub_category_list, name="edusubcatlistlist"),
    path('edusubcat/<int:id>', education_sub_category, name="edusubcat"),
    path('edusubcatfilter/<int:id>', education_sub_category_by_cat, name="edusubcatfilter"),

    path('edulistlist', education_list, name="edulistlist"),
    path('edu/<int:id>', education, name="edu"),
    path('edufiltercat/<int:id>', education_by_cat, name="edufiltercat"),
    path('edufiltersubcat/<int:id>', education_by_sub_cat, name="edufiltersubcat"),

    path('newscatlist', newscat_list, name="newscatlistapi"),
    path('newscat/<int:id>', newscat, name="newscatapi"),

    path('newslist', news_list, name="newslistapi"),
    path('news/<int:id>', news, name="newsapi"),
]