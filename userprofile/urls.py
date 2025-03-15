from django.urls import path
from userprofile import views
from .views import RegisterUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "userprofile"

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('get/token/',views.GetAccessTokenView.as_view(),name='get_access_token'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]