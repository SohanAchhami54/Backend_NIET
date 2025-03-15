# from django.contrib import admin
# from .models import Batch, Semester, BatchSemester, Subject, Student, StudentInSemester, ExamType, SubjectInternalExam, StudentInternalExamResult, StudentSubjectAttendance, Teacher, SubjectTeacher,ExamSession,Notice

# @admin.register(Batch)
# class BatchAdmin(admin.ModelAdmin):
#     list_display = ('year', 'is_active', 'created_at', 'updated_at')
#     search_fields = ('year',)
#     list_filter = ('is_active',)

# @admin.register(Semester)
# class SemesterAdmin(admin.ModelAdmin):
#     list_display = ('number', 'created_at', 'updated_at')
#     search_fields = ('number',)
#     list_filter = ('number',)

# @admin.register(BatchSemester)
# class BatchSemesterAdmin(admin.ModelAdmin):
#     list_display = ('batch', 'semester', 'start_month', 'end_month',  'created_at', 'updated_at')
#     search_fields = ('batch__year', 'semester__number')
#     list_filter = ('batch__year', 'semester__number',)

# @admin.register(Subject)
# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ('name', 'code', 'semester', 'created_at', 'updated_at')
#     search_fields = ('name', 'code')
#     list_filter = ('semester__number',)

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('first_name','last_name','password' ,'photo', 'registration_number', 'created_at', 'updated_at')
#     search_fields = ('first_name','last_name', 'registration_number')
#     list_filter = ('is_active',)

# @admin.register(StudentInSemester)
# class StudentInSemesterAdmin(admin.ModelAdmin):
#     list_display = ('student', 'get_batch','get_semester','is_current', 'created_at', 'updated_at')
#     search_fields = ('student__first_name', 'semester__number')
#     list_filter = ('is_active',)
#     def get_batch(self,obj):
#         return obj.semester.batch.year
#     def get_semester(self,obj):
#         return obj.semester.semester.number

# @admin.register(ExamType)
# class ExamTypeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created_at', 'updated_at')
#     search_fields = ('name',)
#     list_filter = ('is_active',)

# @admin.register(SubjectInternalExam)
# class SubjectInternalExamAdmin(admin.ModelAdmin):
#     list_display = ('subject', 'exam_type', 'full_marks', 'pass_marks', 'created_at', 'updated_at')
#     search_fields = ('subject__name', 'exam_type__name')
#     list_filter = ('is_active',)

# @admin.register(ExamSession)
# class ExamSessionAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)


# @admin.register(StudentInternalExamResult)
# class StudentInternalExamResultAdmin(admin.ModelAdmin):
#     list_display = ('student', 'subject_internalexam', 'marks_obtained','exam_session' ,'created_at', 'updated_at')
#     search_fields = ('student__first_name', 'subject_internalexam__subject__name')
#     list_filter = ('is_active',)

# @admin.register(StudentSubjectAttendance)
# class StudentSubjectAttendanceAdmin(admin.ModelAdmin):
#     list_display = ('student', 'subject', 'day', 'status')
#     search_fields = ('student__first_name', 'subject__name')
#     list_filter = ('status',)

# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'created_at', 'updated_at')
#     search_fields = ('full_name',)
#     list_filter = ('is_active',)

# @admin.register(SubjectTeacher)
# class SubjectTeacherAdmin(admin.ModelAdmin):
#     list_display = ('teacher', 'subject', 'created_at', 'updated_at')
#     search_fields = ('teacher__full_name', 'subject__name')
#     list_filter = ('is_active',)

# @admin.register(Notice)
# class NoticeAdmin(admin.ModelAdmin):
#     list_display = ('semester','message','attachments')
#     search_fields = ('semester__batch__year',)
