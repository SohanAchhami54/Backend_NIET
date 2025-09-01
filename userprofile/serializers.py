from rest_framework import serializers

from userprofile.models import AppUser,UserType

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data['email'] = self.user.email
        data['user_type'] = 'Superuser' if self.user.is_superuser else getattr(self.user.usertype, 'name', None)
        
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Custom claims
        token['email'] = user.email
        token['user_type'] = 'Superuser' if user.is_superuser else getattr(user.usertype, 'name', None)
        return token


class AppUserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('id','email',)

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ('id','name')

class AppUserDetailSerializer(serializers.ModelSerializer):
    usertype = UserTypeSerializer()
    class Meta:
        model = AppUser
        fields = ('id','email','usertype')

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('id','email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = AppUser.objects.create_user(**validated_data)
        return user

