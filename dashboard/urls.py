from django.urls import path
from dashboard import views


app_name = "dashboard"
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('bulk/upload/student/', views.bulk_upload_students, name='bulk_upload_students'),
    path('bulk/upload/faculty/', views.bulk_upload_faculty, name='bulk_upload_faculty'),

] 