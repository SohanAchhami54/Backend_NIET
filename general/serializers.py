from rest_framework import serializers
from general.models import *

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

class CoverImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverImage
        fields = '__all__'

class SliderHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderHome
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'



class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'