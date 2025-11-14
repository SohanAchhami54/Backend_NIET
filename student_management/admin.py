from django.contrib import admin
from student_management.models import *


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

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

@admin.register(UniversityDegree)
class UniversityDegreeAdmin(admin.ModelAdmin):
    list_display = ('university', 'degree', 'is_active')
    list_filter = ('university', 'degree', 'is_active')

@admin.register(AcademicBatch)
class AcademicBatchAdmin(admin.ModelAdmin):
    list_display = ('year', 'is_active', 'created_at')
    search_fields = ('year',)
    list_filter = ('is_active',)

@admin.register(AcademicSemester)
class AcademicSemesterAdmin(admin.ModelAdmin):
    list_display = ('number', 'is_active')
    list_filter = ('is_active',)

@admin.register(DegreeBatch)
class DegreeBatchAdmin(admin.ModelAdmin):
    list_display = ('university_degree', 'academic_batch', 'is_active')
    list_filter = ('is_active',)

@admin.register(DegreeSemester)
class DegreeSemesterAdmin(admin.ModelAdmin):
    list_display = ('university_degree', 'academic_semester', 'is_active')
    list_filter = ('is_active',)

@admin.register(BatchSemester)
class BatchSemesterAdmin(admin.ModelAdmin):
    list_display = ('degree_batch', 'academic_semester', 'start_date', 'end_date', 'is_running', 'is_active')
    list_filter = ('is_running', 'is_active')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'registration_number', 'is_active')
    search_fields = ('first_name', 'last_name', 'registration_number')
    list_filter = ('is_active',)

@admin.register(StudentBatchSemester)
class StudentBatchSemesterAdmin(admin.ModelAdmin):
    list_display = ('student','get_degree_batch' ,'batch_semester', 'section', 'is_active')
    list_filter = ('is_active',)
    def get_degree_batch(self,obj):
        return obj.batch_semester.degree_batch.academic_batch

@admin.register(AcademicSubject)
class AcademicSubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'degree_semester', 'is_active')
    search_fields = ('name', 'code')
    list_filter = ('is_active',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'designation', 'education', 'is_active')
    search_fields = ('full_name', 'designation')
    list_filter = ('is_active',)

@admin.register(SubjectTeacher)
class SubjectTeacherAdmin(admin.ModelAdmin):
    list_display = ('get_degree_semester','academic_subject', 'teacher', 'is_active')
    list_filter = ('is_active',)
    def get_degree_semester(self,obj):
        return obj.academic_subject.degree_semester

@admin.register(SubjectAttendance)
class SubjectAttendanceAdmin(admin.ModelAdmin):
    list_display = ('batch_semester', 'academic_subject', 'day', 'is_active')
    list_filter = ('day', 'is_active')

@admin.register(StudentSubjectAttendanceRecord)
class StudentSubjectAttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('subject_attendance', 'student_batch_semester', 'day', 'status', 'is_active')
    list_filter = ('status', 'day', 'is_active')

@admin.register(StudentAttendanceRecord)
class StudentAttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'academic_subject', 'is_active')
    list_filter = ('is_active',)

@admin.register(StudentGradeSheet)
class StudentGradeSheetAdmin(admin.ModelAdmin):
    list_display = ('student_batch_semester', 'is_active')
    list_filter = ('is_active',)


@admin.register(ExternalExamType)
class ExternalExamTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name',)

@admin.register(ExternalExamResult)
class ExternalExamResultAdmin(admin.ModelAdmin):
    list_display = ('program', 'year_semester', 'exam_type', 'examination_held_on', 'result_published_date')
    search_fields = ('program', 'year_semester', 'exam_type')
    list_filter = ('exam_type',)

@admin.register(ExternalExamResultContent)
class ExternalExamResultContentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'symbol_number', 'registration_number', 'sgpa', 'pass_fail')
    search_fields = ('student_name', 'symbol_number', 'registration_number')
    list_filter = ('pass_fail',)

@admin.register(ExternalExamResultScore)
class ExternalExamResultScoreAdmin(admin.ModelAdmin):
    list_display = ('external_result_content', 'subject', 'score')
    search_fields = ('subject',)
    list_filter = ('subject',)

@admin.register(BatchSemesterNotice)
class BatchSemesterNoticeAdmin(admin.ModelAdmin):
    list_display = ('batch_semester', 'title', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title', 'messages')
    list_filter = ('is_active', 'created_at', 'updated_at')


@admin.register(StudentInternalExamResult)
class StudentInternalExamResultAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'academic_subject',
        'batch_semester',
        'record',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = ('academic_subject', 'batch_semester', 'is_active', 'created_at')
    search_fields = ('academic_subject__name', 'batch_semester__name')  # Adjust field names as per related models
    readonly_fields = ('created_at', 'updated_at')

@admin.register(StudentInternalExamResultContent)
class StudentInternalExamResultContentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student_internalexam_result',
        'student_batch_semester',
        'marks_obtained',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = ('student_internalexam_result', 'student_batch_semester', 'is_active', 'created_at')
    search_fields = ('marks_obtained', 'student_batch_semester__student__name')  # Adjust as needed
    readonly_fields = ('created_at', 'updated_at')

