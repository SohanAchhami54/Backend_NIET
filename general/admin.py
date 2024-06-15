from django.contrib import admin
from .models import (
    HomeVideo, HomeImages, AboutImages, AboutCertificates, AboutUs, FacultyType,
    Faculty, ProjectCategory, News, Vaccancy,
    NoticeAndResult, ContactMessage, Faq,Chairman,Gallery,Home,Feature,MissionPartners
)

@admin.register(HomeVideo)
class HomeVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url')
    search_fields = ('title',)

@admin.register(HomeImages)
class HomeImagesAdmin(admin.ModelAdmin):
    list_display = ('title_1', 'photo_1')
    search_fields = ('title_1',)

@admin.register(AboutImages)
class AboutImagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo')
    search_fields = ('title',)

@admin.register(AboutCertificates)
class AboutCertificatesAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo')
    search_fields = ('title',)

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'affiliation', 'registration', 'is_active', 'created_at', 'updated_at')
    search_fields = ('full_name', 'affiliation', 'registration')
    list_filter = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(FacultyType)
class FacultyTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'is_active', 'created_at', 'updated_at')
    search_fields = ('type_name',)
    list_filter = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name', 'education', 'designation', 'email', 'is_active', 'created_at', 'updated_at')
    # search_fields = ('name', 'education', 'designation', 'email')
    # list_filter = ('is_active',)
    # readonly_fields = ('created_at', 'updated_at')


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'is_active', 'created_at', 'updated_at')
    search_fields = ('type_name',)
    list_filter = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Vaccancy)
class VaccancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(NoticeAndResult)
class NoticeAndResultAdmin(admin.ModelAdmin):
    list_display = ('title', 'any_url', 'is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'any_url')
    list_filter = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'is_active', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'answer_text')
    search_fields = ('question_text', 'answer_text')

@admin.register(Chairman)
class ChairmanAdmin(admin.ModelAdmin):
    list_display = ('faculty',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('description',)

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('why_biomedical',)

@admin.register(MissionPartners)
class MissionPartnersAdmin(admin.ModelAdmin):
    list_display = ('name',)




