from rest_framework import serializers

from userprofile.models import AppUser

class AppUserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('id','email',)

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('id','email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = AppUser.objects.create_user(**validated_data)
        return user

