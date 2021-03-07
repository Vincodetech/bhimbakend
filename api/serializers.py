from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator
from home.models import CustomUser
from home.models import Profile
from home.models import Country
from home.models import State
from home.models import City
from home.models import EducationCategory
from home.models import EducationSubCategory
from home.models import Education
from home.models import NewsCategory
from home.models import News
from myadmin.models import *
from django.core.files.base import ContentFile
import base64
import six
import uuid
import imghdr

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name','last_name','phone','email','active']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','user']

class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension
        
class UserEditProfileSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = Profile
        fields = ['id','date_of_birth','gender','photo','street1','street2','country','add_state','add_city',
                    'add_block','add_village','add_international','degree','profession_type','title','intrests']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','country_name']

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id','state_name']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','city_name']

class EducationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationCategory
        fields = '__all__'

class EducationSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationSubCategory
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'