from django.urls import path
from userprofile import views
from .views import RegisterUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from userprofile.serializers import MyTokenObtainPairSerializer

app_name = "userprofile"

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('get/token/',views.GetAccessTokenView.as_view(),name='get_access_token'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.GetRefreshTokenView.as_view(), name='token_refresh'),
    path('',views.UsersList.as_view(),name="users_list"),
    path('types/',views.UserTypeList.as_view(),name="user_type_list"),
    path('create/',views.UserCreate.as_view(),name="user_create"),

]