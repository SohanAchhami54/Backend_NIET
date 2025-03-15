from django.urls import path
from student_management import views

app_name="student_management"

urlpatterns = [
    path('university/detail/',views.UniversityDetail.as_view(),name='university_detail'),
    path('degree/detail/',views.DegreeDetail.as_view(),name='degree_detail'),
    path('batch/detail/',views.AcademicBatchDetail.as_view(),name='batch_detail'),
    path('semester/detail/',views.AcademicSemesterDetail.as_view(),name='semester_detail'),
    path('external/exam/type/',views.ExternalExamTypeDetail.as_view(),name='external_exam_type_detail'),
    path('register/student/',views.RegisterStudent.as_view(),name='register_student'),
    path('student/batch/semester/',views.StudentBatchSemesterList.as_view(),name='student_batch_semester_list'),
    path('external/exam/result/',views.ExternalExamResultList.as_view(),name='external_exam_result_list'),
    path('external/exam/result/<int:id>/',views.ExternalExamResultDetail.as_view(),name='external_exam_result'),
    path('external/original/exam/result/<int:id>/',views.ExternalOriginalExamResultDetail.as_view(),name='external_original_exam_result'),
    path('upload/external/exam/result/',views.UploadExternalExamResult.as_view(),name='upload_external_exam_result'),

    # for students 
    path('student/<int:user_id>/',views.StudentDetail.as_view(),name='student_detail'),
    path('student/external/result/<int:user_id>/',views.StudentExternalResultDetail.as_view(),name='student_external_result_detail'),
    # for notices 
    path('semester/notice/create/',views.BatchSemesterNoticeCreate.as_view(),name='semester_notice_create'),
    path('semester/notice/',views.SemesterNoticeList.as_view(),name='notice_list'),
    path('semester/notice/<int:id>/',views.SemesterNoticeDetail.as_view(),name='notice_detail'),
    path('student/semester/notice/',views.StudentNoticeList.as_view(),name='student_notice_list'),


]