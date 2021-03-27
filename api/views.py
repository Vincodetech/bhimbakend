from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from home.models import CustomUser
from home.models import Profile
from home.models import EducationCategory
from home.models import EducationSubCategory
from home.models import Education
from home.models import NewsCategory
from home.models import News
from myadmin.models import *
from .serializers import *
import random
from urllib.request import Request, urlopen 
from urllib.parse import quote
from django.http import HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import parser_classes


def send_sms(phoneno, otp):
    user = "DEMOUSER"
    key = "1b23df7a0aXX"
    mobile = "+91" + phoneno
    message = "Hi, Your verification code is " + str(otp) + " Please do not share it. www.bhimconnect.com"
    msg = quote(message)
    senderid = "vincod"
    url = f"http://sms.vincode.in/submitsms.jsp?user={user}&key={key}&mobile={mobile}&senderid={senderid}&accusage=1&message={msg}"
    req = Request(url=url, method='GET')
    response = urlopen(req)
    output = response.read() 
    print("=======>>", output)

@api_view(['GET'])
def perform_otp_sms(request):
    send_sms(request.GET.get('phone'), request.GET.get('otp'))
    return Response('sent', status=status.HTTP_200_OK)

@api_view(['POST'])
def perform_registration(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        Profile.objects.create(user=user)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def perform_login(request):
    phone = request.data['phone']
    try:
        user = CustomUser.objects.get(phone=phone)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if user:
        serializer = UserSerializer(user)
        return Response(serializer.data)

@api_view(['GET'])
def user_profile(request, id):
    try:
        user_profile = Profile.objects.get(user=id)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        profile_serializer = UserEditProfileSerializer(user_profile)
        return Response(profile_serializer.data)

@api_view(['GET'])
def country_list(request):
    if request.method == 'GET':
        allcountries = Country.objects.all()
        country_serializer = CountrySerializer(allcountries, many=True)
        return Response(country_serializer.data)

@api_view(['GET'])
def state_list(request):
    if request.method == 'GET':
        allstate = State.objects.all()
        state_serializer = StateSerializer(allstate, many=True)
        return Response(state_serializer.data)

@api_view(['GET'])
def city_list(request):
    if request.method == 'GET':
        allcity = City.objects.all()
        city_serializer = CitySerializer(allcity, many=True)
        return Response(city_serializer.data)

@api_view(['POST'])
@parser_classes([FormParser, MultiPartParser])
def updateUserProfile(request, id):
    try:
        user = CustomUser.objects.get(id=id)
        user_profile = Profile.objects.get(user=user)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # if request.method == 'POST':
    profile_serializer = UserEditProfileSerializer(user_profile, data=request.data)
    user_serializer = UserSerializer(user, data=request.data)

    if profile_serializer.is_valid(raise_exception=True) and user_serializer.is_valid(raise_exception=True):
        profile_serializer.save()
        user_serializer.save()
        return Response([profile_serializer.data, user_serializer.data] , 
            status=status.HTTP_201_CREATED)
    else:
        return Response([profile_serializer.errors, user_serializer.errors], 
            status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_user(request, id):
    try:
        user = CustomUser.objects.get(id=id)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)

@api_view(['GET'])
def education_category_list(request):
    edu_cats = EducationCategory.objects.all()
    if request.method == 'GET':
        edu_cat_serializer = EducationCategorySerializer(edu_cats, many=True)
        return Response(edu_cat_serializer.data)

@api_view(['GET'])
def education_category(request, id):
    try:
        single_edu_cat = EducationCategory.objects.get(id=id)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        edu_cat_serializer = EducationCategorySerializer(single_edu_cat)
        return Response(edu_cat_serializer.data)

@api_view(['GET'])
def education_sub_category_list(request):
    edu_sub_cats = EducationSubCategory.objects.all()
    if request.method == 'GET':
        edu_sub_cat_serializer = EducationSubCategorySerializer(edu_sub_cats, many=True)
        return Response(edu_sub_cat_serializer.data)

@api_view(['GET'])
def education_sub_category(request, id):
    try:
        single_edu_sub_cat = EducationSubCategory.objects.get(id=id)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        edu_sub_cat_serializer = EducationSubCategorySerializer(single_edu_sub_cat)
        return Response(edu_sub_cat_serializer.data)

@api_view(['GET'])
def education_sub_category_by_cat(request, id):
    try:
        single_edu_sub_cat = EducationSubCategory.objects.filter(category=id)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        edu_sub_cat_serializer = EducationSubCategorySerializer(single_edu_sub_cat, many=True)
        return Response(edu_sub_cat_serializer.data)

@api_view(['GET'])
def education_list(request):
    edus = Education.objects.all()
    if request.method == 'GET':
        edu_serializer = EducationSerializer(edus, many=True)
        return Response(edu_serializer.data)

@api_view(['GET'])
def education(request, id):
    try:
        single_edu = Education.objects.get(id=id)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        edu_serializer = EducationSerializer(single_edu)
        return Response(edu_serializer.data)

@api_view(['GET'])
def education_by_cat(request, id):
    try:
        edu_by_cat = Education.objects.filter(category=id)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        edu_by_cat_serializer = EducationSerializer(edu_by_cat, many=True)
        return Response(edu_by_cat_serializer.data)

@api_view(['GET'])
def education_by_sub_cat(request, id):
    try:
        edu_by_sub_cat = Education.objects.filter(sub_category=id)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        edu_by_sub_cat_serializer = EducationSerializer(edu_by_sub_cat, many=True)
        return Response(edu_by_sub_cat_serializer.data)

@api_view(['GET'])
def newscat(request, id):
    try:
        newscat = NewsCategory.objects.get(id=id)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        newscat_serializer = NewsCategorySerializer(newscat)
        return Response(newscat_serializer.data)

@api_view(['GET'])
def newscat_list(request):
    newscats = NewsCategory.objects.all()
    if request.method == 'GET':
        newscat_serializer = NewsCategorySerializer(newscats, many=True)
        return Response(newscat_serializer.data)

@api_view(['GET'])
def news(request, id):
    try:
        news = News.objects.get(id=id)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        news_serializer = NewsSerializer(news)
        return Response(news_serializer.data)

@api_view(['GET'])
def news_list(request):
    news = News.objects.all()
    if request.method == 'GET':
        news_serializer = NewsSerializer(news, many=True)
        return Response(news_serializer.data)