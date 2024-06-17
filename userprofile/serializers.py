from rest_framework import serializers

from userprofile.models import AppUser



class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('id','first_name','middle_name','last_name','email', 'password')
        extra_kwargs = {'password': {'write_only': True}}