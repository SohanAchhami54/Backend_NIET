from django.contrib import admin
from general.models import (
    MissionPartners, HomeVideo, HomeImages, Feature, Home, AboutImages, 
    AboutCertificates, AboutUs, FacultyType, Faculty, Chairman, ProjectCategory, 
    News, Vaccancy, Notice, Result, ContactMessage, Faq, Gallery,CoverImage,Syllabus,EntranceSyllabus,EligiblityCriteria,SliderHome
)

@admin.register(MissionPartners)
class MissionPartnersAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo']
    search_fields = ['name']

@admin.register(HomeVideo)
class HomeVideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_url']
    search_fields = ['title']

@admin.register(CoverImage)
class CoverImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo', ]
    search_fields = ['title', 'photo', ]

@admin.register(SliderHome)
class SliderHomeAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo', ]
    search_fields = ['title', 'photo',]


@admin.register(HomeImages)
class HomeImagesAdmin(admin.ModelAdmin):
    list_display = ['title_1', 'photo_1', 'title_2', 'photo_2']
    search_fields = ['title_1', 'title_2']

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'feature_text', 'feature_img']
    search_fields = ['title']

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['why_biomedical', 'why_photo']
    search_fields = ['why_biomedical']

# @admin.register(AboutImages)
# class AboutImagesAdmin(admin.ModelAdmin):
#     list_display = ['title', 'photo']
#     search_fields = ['title']

# @admin.register(AboutCertificates)
# class AboutCertificatesAdmin(admin.ModelAdmin):
#     list_display = ['title', 'photo']
#     search_fields = ['title']

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'short_name', 'logo', 'affiliation', 'registration', 'is_active']
    search_fields = ['full_name', 'short_name', 'affiliation', 'registration']
    list_filter = ['is_active', 'created_at', 'updated_at']

@admin.register(FacultyType)
class FacultyTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name', 'is_active']
    search_fields = ['type_name']
    list_filter = ['is_active', 'created_at', 'updated_at']

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo', 'education', 'designation', 'post_name', 'faculty_type', 'linkedin_url', 'is_active']
    search_fields = ['user__first_name', 'user__last_name', 'education', 'designation', 'post_name', 'faculty_type__type_name']
    list_filter = ['is_active', 'created_at', 'updated_at']

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title',]

@admin.register(EntranceSyllabus)
class EntranceSyllabusAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title',]

@admin.register(EligiblityCriteria)
class EligiblityCriteriaAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title',]

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['type_name', 'is_active']
    search_fields = ['type_name']
    list_filter = ['is_active', 'created_at', 'updated_at']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo', 'pdf', 'slug', 'is_active']
    search_fields = ['title']
    list_filter = ['is_active', 'created_at', 'updated_at']
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Vaccancy)
class VaccancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo', 'pdf', 'slug', 'display_as_new', 'is_active']
    search_fields = ['title']
    list_filter = ['is_active', 'created_at', 'updated_at', 'display_as_new']
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo', 'pdf', 'any_url', 'slug', 'display_as_new', 'is_active']
    search_fields = ['title']
    list_filter = ['is_active', 'created_at', 'updated_at', 'display_as_new']
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo', 'pdf', 'any_url', 'slug', 'display_as_new', 'is_active']
    search_fields = ['title']
    list_filter = ['is_active', 'created_at', 'updated_at', 'display_as_new']
    prepopulated_fields = {"slug": ("title",)}

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'is_active']
    search_fields = ['full_name', 'email', 'phone_number', 'is_active']
    list_filter = ['is_active', 'created_at', 'updated_at']

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'answer_text']
    search_fields = ['question_text', 'answer_text']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['description', 'photo', 'is_active']
    search_fields = ['description']
    list_filter = ['is_active', 'created_at', 'updated_at']
