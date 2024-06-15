from django.urls import path
from academic import views


app_name = "academic"
urlpatterns = [
    path("admin/",views.admin_dashboard,name='dashboard'),
    path('bulk/upload/student/', views.bulk_upload_students, name='bulk_upload_students'),
    path('bulk/upload/faculty/', views.bulk_upload_faculty, name='bulk_upload_faculty'),
] 