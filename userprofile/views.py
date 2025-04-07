from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from userprofile.models import AppUser
from userprofile.serializers import AppUserSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import AnonymousUser


# Create your views here.

class GetAccessTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        refresh = RefreshToken.for_user(request.user)
        access_token = refresh.access_token

        # Manually add custom claims
        
        access_token['email'] = request.user.email
        if request.user.is_superuser:
            access_token['user_type'] = 'Superuser'
        else:
            if hasattr(request.user, 'usertype'):
                access_token['user_type'] = request.user.usertype.name if request.user.usertype else None

        return Response({
            "access": str(access_token),
            "refresh": str(refresh)
        })

class GetRefreshTokenView(APIView):
    permission_classes = [IsAuthenticated]  

    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response({"detail": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Decode the refresh token
            refresh = RefreshToken(refresh_token)

            # Get user from the token
            user = refresh.user
            if not user or isinstance(user, AnonymousUser):
                return Response({"detail": "Invalid user."}, status=status.HTTP_401_UNAUTHORIZED)

            # Generate new access token
            access_token = refresh.access_token

            # Add custom claims
            access_token["email"] = user.email
            if user.is_superuser:
                access_token["user_type"] = "Superuser"
            else:
                if hasattr(user, "usertype"):
                    access_token["user_type"] = user.usertype.name if user.usertype else None

            return Response({
                "access": str(access_token)
            })

        except Exception as e:
            return Response({"detail": "Invalid refresh token."}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterUserView(APIView):
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    def post(self, request):

        # if email is already in use
        if AppUser.objects.filter(email=request.data['email']).exists():
            return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = AppUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserView(APIView):
#     permission_classes = (IsAuthenticated,)
#     parser_classes = [JSONParser, MultiPartParser, FormParser]

#     def get(self, request):
#         serializer = UserProfileSerializer(request.user, many=False)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # update user profile image
#     def put(self, request):
#         user = UserProfile.objects.get(email=request.user.email)
#         user.avatar = request.data['avatar']
#         user.save()
#         return Response({'message': 'Image updated'}, status=status.HTTP_200_OK)
