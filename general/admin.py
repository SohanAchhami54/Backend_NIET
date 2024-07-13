from django.contrib import admin
from .models import (
    CoverImage, SliderHome, Feature, AboutUs, StaffType, Staff, CollegeChairman,
    Syllabus, EntranceSyllabus, EligiblityCriteria, ProjectCategory, News,
    Vaccancy, Notice, Result, ContactMessage, Faq, Gallery,Testimonial,VideoTestimonial
)

@admin.register(CoverImage)
class CoverImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)


@admin.register(SliderHome)
class SliderHomeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'feature_text', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title', 'feature_text')
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'short_name', 'affiliation', 'registration', 'created_at', 'updated_at', 'is_active')
    search_fields = ('full_name', 'short_name', 'affiliation', 'registration')
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)


@admin.register(StaffType)
class StaffTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'created_at', 'updated_at', 'is_active')
    search_fields = ('type_name',)
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'designation', 'post_name', 'staff_type', 'created_at', 'updated_at', 'is_active')
    search_fields = ('full_name', 'designation', 'post_name')
    list_filter = ('is_active', 'created_at', 'staff_type')
    ordering = ('-created_at',)


@admin.register(CollegeChairman)
class CollegeChairmanAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'created_at', 'updated_at', 'is_active')
    search_fields = ('full_name', )
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)


@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)


@admin.register(EntranceSyllabus)
class EntranceSyllabusAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)


@admin.register(EligiblityCriteria)
class EligiblityCriteriaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'created_at', 'updated_at', 'is_active')
    search_fields = ('type_name',)
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)


@admin.register(Vaccancy)
class VaccancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'display_as_new', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active', 'display_as_new', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'display_as_new', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active', 'display_as_new', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'display_as_new', 'created_at', 'updated_at', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active', 'display_as_new', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'subject', 'created_at', 'updated_at', 'is_active')
    search_fields = ('full_name', 'email', 'phone_number', 'subject')
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question_text',)
    search_fields = ('question_text',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at', 'updated_at', 'is_active')
    search_fields = ('description',)
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name','description', 'created_at', 'updated_at', 'is_active')
    search_fields = ('description',)
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)


@admin.register(VideoTestimonial)
class VideoTestimonialAdmin(admin.ModelAdmin):
    list_display = ('video_url','description', 'created_at', 'updated_at', 'is_active')
    search_fields = ('description',)
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)



