# from django.urls import path
# from management import views

# app_name="management"

# urlpatterns = [
#     path("login/",views.handle_login,name='handle_login'),
#     path("logout/",views.handle_logout,name='handle_logout'),
#     path("admin/",views.handle_admin,name='handle_admin'),
#     path("student/",views.handle_student,name='handle_student'),
#     path("teacher/",views.handle_teacher,name='handle_teacher'),
#     path('register/student/',views.RegisterStudent.as_view(),name='register_student'),
#     path('register/teacher/',views.RegisterTeacher.as_view(),name='register_teacher'),
#     path('password/reset/',views.PasswordReset.as_view(),name='pasword_reset'),
#     # apis 

#     path('exam/types/',views.ExamTypeList.as_view(),name="exam_type_list"),
#     path('exam/session/',views.ExamSessionList.as_view(),name="exam_session_list"),
#     path('internal/exam/marks/update/',views.StudentInternalExamMarksUpdate.as_view(),name='internal_exam_marks_update'),

#     # now 
#     path('batch/lists/',views.BatchList.as_view(),name='batch_list'),
#     path('semester/lists/',views.SemesterList.as_view(),name='semester_list'),
#     path('batch/semester/detail/',views.BatchSemesterDetail.as_view(),name="batch_semester_detail"),
#     path('batch/semester/history/<str:year>/',views.BatchSemesterHistory.as_view(),name="batch_semester_history"),
#     path('batch/semester/filter/<int:id>/',views.BatchSemesterFilter.as_view(),name="batch_semester_Filter"),
#     path('student/batch/semester/<int:batch_id>/<int:semester_id>/',views.StudentBatchSemesterList.as_view(),name='student_batchsemester_list'),

#     # now ends 

#     path('teacher/lists/',views.TeacherList.as_view(),name='teacher_list'),
#     path('batch/semester/lists/',views.BatchSemesterList.as_view(),name='batch_semester_list'),
#     path('subject/lists/<int:sem_id>/',views.SubjectList.as_view(),name='subject_list'),
#     path('subject/lists/batch/semester/<int:batch_sem_id>/',views.SubjectListBatchSemester.as_view(),name='subject_list_batchsemester'),
#     path('student/lists/batch/semester/<int:batch_sem_id>/',views.StudentListBatchSemester.as_view(),name='student_list_batchsemester'),
#     path('student/bulk/attendance/',views.StudentBulkAttendance.as_view(),name='student_bulk_attendance'),
#     path('subject/teacher/lists/<int:sem_id>/',views.SubjectTeacherList.as_view(),name='subject_teacher_list'),
#     path('subject/teacher/lists/',views.SubjectTeacherListDetail.as_view(),name='subject_teacher_listdetail'),
#     path('assign/subject/teacher/',views.AssignSubjectTeacher.as_view(),name='assign_subject_teacher'),
#     path('upgrade/student/',views.UpgradeStudent.as_view(),name='upgrade_student'),
#     path('assign/student/',views.AssignStudent.as_view(),name='assign_student'),
#     path('student/notice/list/',views.StudentNoticeList.as_view(),name='student_notice_list'),
#     path('individual/student/record/<int:batch_sem_id>/<int:student_id>/',views.IndividualStudentRecord.as_view(),name='individual_student_record'),
#     path('attendance/record/list/<int:subject_id>/',views.AttendanceRecordList.as_view(),name='attendance_record_list'),
#     # path('update/subject/teacher/<int:id>/<int:subject_id>/<int:teacher_id>/',views.UpdateSubjectTeacher.as_view(),name='update_subject_teacher'),

#     path('student/current/attendance/record/',views.StudentCurrentAttendanceRecord.as_view(),name='student_attendance_record'),
#     path('student/internal/exam/record/',views.StudentInternalExamRecord.as_view(),name='student_internalexam_record'),
#     path('student/record/upload/',views.StudentRecordUpload.as_view(),name='student_record_upload'),
#     path('student/internal/exam/marks/list/',views.StudentStudentInternalExamMarksList.as_view(),name='student_internalexam_marks_list'),
# ]