from django.contrib import admin
from dashboard.models import (
     Student, YearlyScheduler, StudentYearlyScheduler,
    Subject, SubjectSchedule, TheoryInternalMarks,
    PracticalInternalMarks,Batch,Schedule
)

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'passed_year', 'admission_year', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'passed_year', 'admission_year')
    search_fields = ('name',)
    ordering = ('-created_at',)

# @admin.register(StudentsBatch)
# class StudentsBatchAdmin(admin.ModelAdmin):
#     pass
    # list_display = ('name', 'passed_year', 'admission_year', 'is_active', 'created_at', 'updated_at')
    # list_filter = ('is_active', 'passed_year', 'admission_year')
    # search_fields = ('name',)
    # ordering = ('-created_at',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'registration_number',  'is_alumni', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'is_alumni',)
    search_fields = ('user__first_name', 'user__last_name', 'registration_number')
    ordering = ('-created_at',)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('year_part',  'semester_part',)
    search_fields = ('year_part',  'semester_part', )

@admin.register(YearlyScheduler)
class YearlyScheduleAdmin(admin.ModelAdmin):
    list_display = ('year',  'remarks')
    search_fields = ('year', )

@admin.register(StudentYearlyScheduler)
class StudentYearlySchedulerAdmin(admin.ModelAdmin):
    list_display = ('yearly_schedule',)
    search_fields = ('yearly_schedule__year',)

# @admin.register(Publication)
# class PublicationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'country')
#     search_fields = ('name', 'country')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    list_filter = ('code',)

@admin.register(SubjectSchedule)
class SubjectScheduleAdmin(admin.ModelAdmin):
    list_display = ('subject', 'schedule')
    search_fields = ('subject__name',)

@admin.register(TheoryInternalMarks)
class TheoryInternalMarksAdmin(admin.ModelAdmin):
    list_display = ('student_yearly_scheduler', 'subject', 'internal_assessment', 'attendance', 'class_performance', 'assignment', 'presentation')
    search_fields = ('student_yearly_scheduler__student__user__first_name', 'student_yearly_scheduler__student__user__last_name', 'subject__subject__name')
    list_filter = ('subject',)

@admin.register(PracticalInternalMarks)
class PracticalInternalMarksAdmin(admin.ModelAdmin):
    list_display = ('student_yearly_scheduler', 'subject', 'labexam_viva', 'attendance', 'lab_report')
    search_fields = ('student_yearly_scheduler__student__user__first_name', 'student_yearly_scheduler__student__user__last_name', 'subject__subject__name')
    list_filter = ('subject',)