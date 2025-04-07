from django.contrib import admin
from .models import (
    University, Degree, UniversityDegree, AcademicBatch, AcademicSemester, DegreeBatch, DegreeSemester,
    BatchSemester, Student, StudentBatchSemester, AcademicSubject, Teacher, SubjectTeacher,
    StudentSubjectAttendanceRecord, StudentAttendanceRecord, ExternalExamType,ExternalExamResult,
    BatchSemesterNotice
)

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

@admin.register(UniversityDegree)
class UniversityDegreeAdmin(admin.ModelAdmin):
    list_display = ('degree', 'university', 'is_active', 'created_at')
    search_fields = ('degree__name', 'university__name')
    list_filter = ('is_active',)

@admin.register(AcademicBatch)
class AcademicBatchAdmin(admin.ModelAdmin):
    list_display = ('year', 'is_active', 'created_at')
    search_fields = ('year',)
    list_filter = ('is_active',)

@admin.register(AcademicSemester)
class AcademicSemesterAdmin(admin.ModelAdmin):
    list_display = ('number', 'is_active', 'created_at')
    search_fields = ('number',)
    list_filter = ('is_active',)

@admin.register(DegreeBatch)
class DegreeBatchAdmin(admin.ModelAdmin):
    list_display = ('university_degree', 'academic_batch', 'is_active', 'created_at')
    search_fields = ('university_degree__degree__name', 'academic_batch__year')
    list_filter = ('is_active',)

@admin.register(DegreeSemester)
class DegreeSemesterAdmin(admin.ModelAdmin):
    list_display = ('university_degree', 'academic_semester', 'is_active', 'created_at')
    search_fields = ('university_degree__degree__name', 'academic_semester__number')
    list_filter = ('is_active',)

@admin.register(BatchSemester)
class BatchSemesterAdmin(admin.ModelAdmin):
    list_display = ('degree_batch', 'academic_semester', 'start_month', 'end_month', 'is_running')
    search_fields = ('degree_batch__university_degree__degree__name', 'academic_semester__number')
    list_filter = ('is_running', 'is_active')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'registration_number', 'is_active', 'created_at')
    search_fields = ('first_name', 'last_name', 'registration_number')
    list_filter = ('is_active',)

@admin.register(StudentBatchSemester)
class StudentBatchSemesterAdmin(admin.ModelAdmin):
    list_display = ('student', 'batch_semester', 'is_active', 'created_at')
    search_fields = ('student__first_name', 'student__last_name', 'batch_semester__academic_semester__number')
    list_filter = ('is_active',)

@admin.register(AcademicSubject)
class AcademicSubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'degree_semester', 'is_active', 'created_at')
    search_fields = ('name', 'code')
    list_filter = ('is_active',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'is_active', 'created_at')
    search_fields = ('full_name',)
    list_filter = ('is_active',)

@admin.register(SubjectTeacher)
class SubjectTeacherAdmin(admin.ModelAdmin):
    list_display = ('academic_subject', 'teacher', 'is_active', 'created_at')
    search_fields = ('academic_subject__name', 'teacher__full_name')
    list_filter = ('is_active',)

# @admin.register(StudentSubjectAttendance)
# class StudentSubjectAttendanceAdmin(admin.ModelAdmin):
#     list_display = ('student_batch_semester', 'academic_subject', 'day', 'status', 'is_active')
#     search_fields = ('student_batch_semester__student__first_name', 'academic_subject__name')
#     list_filter = ('status', 'is_active')

@admin.register(StudentAttendanceRecord)
class StudentAttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'academic_subject', 'is_active', 'created_at')
    search_fields = ('student__first_name', 'academic_subject__name')
    list_filter = ('is_active',)

@admin.register(ExternalExamType)
class ExternalExamTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

@admin.register(ExternalExamResult)
class ExternalExamResultAdmin(admin.ModelAdmin):
    list_display = ('exam_type',  'examination_held_on', 'result_published_date',)
    search_fields = ('exam_type','examination_held_on', 'result_published_date', )


@admin.register(BatchSemesterNotice)
class BatchSemesterNoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'batch_semester', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title', 'batch_semester__degree_batch__university_degree__degree__name', 'batch_semester__academic_semester__number')


admin.site.site_header = "University Management Admin"
admin.site.site_title = "University Management"
admin.site.index_title = "Admin Dashboard"
