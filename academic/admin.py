from django.contrib import admin
from .models import (
    StudentBatch, Student, YearlySchedule, StudentYearlySchedule,
    Publication, Subject, SubjectYearlySchedule, TheoryInternalMarks,
    PracticalInternalMarks
)

@admin.register(StudentBatch)
class StudentBatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'passed_year', 'admission_year', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'passed_year', 'admission_year')
    search_fields = ('name',)
    ordering = ('-created_at',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'registration_number', 'batch', 'is_alumni', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'is_alumni', 'batch')
    search_fields = ('user__first_name', 'user__last_name', 'registration_number')
    ordering = ('-created_at',)

@admin.register(YearlySchedule)
class YearlyScheduleAdmin(admin.ModelAdmin):
    list_display = ('year', 'month_from_to', 'year_part', 'semester_part', 'remarks')
    search_fields = ('year', 'year_part', 'semester_part')

@admin.register(StudentYearlySchedule)
class StudentYearlyScheduleAdmin(admin.ModelAdmin):
    list_display = ('yearly_schedule',)
    search_fields = ('yearly_schedule__year',)

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'publication')
    search_fields = ('name', 'author')
    list_filter = ('publication',)

@admin.register(SubjectYearlySchedule)
class SubjectYearlyScheduleAdmin(admin.ModelAdmin):
    list_display = ('subject', 'yearly_schedule')
    search_fields = ('subject__name', 'yearly_schedule__year')

@admin.register(TheoryInternalMarks)
class TheoryInternalMarksAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'internal_assessment', 'attendance', 'class_performance', 'assignment', 'presentation')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'subject__subject__name')
    list_filter = ('subject',)

@admin.register(PracticalInternalMarks)
class PracticalInternalMarksAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'labexam_viva', 'attendance', 'lab_report')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'subject__subject__name')
    list_filter = ('subject',)