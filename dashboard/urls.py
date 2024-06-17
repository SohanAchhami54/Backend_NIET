from django.urls import path
from dashboard import views


app_name = "dashboard"
urlpatterns = [
    # path("admin/",views.admin_dashboard,name='dashboard'),
    # path('bulk/upload/student/', views.bulk_upload_students, name='bulk_upload_students'),
    # path('bulk/upload/faculty/', views.bulk_upload_faculty, name='bulk_upload_faculty'),
    path("yearly/schedule/",views.YearlyScheduleList.as_view(),name='YearlyScheduleList'),
    path('student/yearly/schedule/', views.StudentYearlyScheduleUpload.as_view(), name='student-yearly-schedule-upload'),
    path('student/yearly/schedule/list/<int:schedule_id>/', views.StudentYearlyScheduleList.as_view(), name='student-yearly-schedule-list'),
    path('student/yearly/schedule/update/', views.StudentYearlyScheduleUpdate.as_view(), name='student-yearly-schedule-update'),


] 