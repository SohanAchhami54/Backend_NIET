from django.urls import path
from student_management import views

app_name="student_management"

urlpatterns = [
    path('university/detail/',views.UniversityDetail.as_view(),name='university_detail'),
    path('degree/detail/',views.DegreeDetail.as_view(),name='degree_detail'),
    path('section/detail/',views.SectionDetail.as_view(),name='section_detail'),
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
    path('student/semester/<int:user_id>/',views.StudentSemesterList.as_view(),name='student_semester_list'),
    path('student/external/result/<int:user_id>/',views.StudentExternalResultDetail.as_view(),name='student_external_result_detail'),
    # for notices 
    path('semester/notice/create/',views.BatchSemesterNoticeCreate.as_view(),name='semester_notice_create'),
    path('semester/notice/',views.SemesterNoticeList.as_view(),name='notice_list'),
    path('semester/notice/<int:id>/',views.SemesterNoticeDetail.as_view(),name='notice_detail'),
    path('student/semester/notice/',views.StudentNoticeList.as_view(),name='student_notice_list'),

    # for teacher 
    path('register/faculty/',views.RegisterFaculty.as_view(),name='register_faculty'),
    path('teacher/',views.TeacherList.as_view(),name='teacher_list'),
    path('teacher/<int:id>/',views.TeacherDetail.as_view(),name='teacher_detail'),
    path('teacher/detail/<int:id>/',views.TeacherDetailById.as_view(),name='teacher_detail_byId'),


    path('assigned/teacher/subject/<int:id>/',views.AssignedTeacherSubjectList.as_view(),name='teacher_subject_list'),
    path('assigned/teacher/running/subject/',views.AssignedTeacherRunningSubjectList.as_view(),name='teacher_running_subject_list'),
    path('take/student/attendance/',views.TakeStudentAttendance.as_view(),name='take_student_attendance'),
    path('student/attendance/update/<int:id>/',views.StudentAttendanceUpdate.as_view(),name='student_attendance_update'),

    path('subject/attendance/list/',views.SubjectAttendanceList.as_view(),name='subject_attendance_list'),
    path('attendance/record/list/<int:id>/<int:section>/',views.AttendanceRecordList.as_view(),name='attendance_record_list'),
    path('attendance/daywise/update/',views.DayWiseAttendanceRecordUpdate.as_view(),name='daywise_attendance_update'),

    # for admin view
    path('student/attendance/summary/',views.StudentAttendanceSummary.as_view(),name='student_attendance_summary'), 
    path('student/admin/summary/<int:id>/',views.StudentAdminSummary.as_view(),name='student_admin_summary'),
    path('student/gradesheet/upload/',views.StudentGradeSheetUpload.as_view(),name='student_gradesheet_upload'),
    path('student/gradesheet/summary/<int:id>/',views.StudentGradeSheetSummary.as_view(),name='student_admin_summary'),
    path('student/subject/attendance/list/',views.StudentSubjectAttendanceList.as_view(),name='student_subject_attendance_list'),

    
    path('academic/subject/<str:semester_number>/',views.AcademicSubjectList.as_view(),name='academic_subject_list'),

]