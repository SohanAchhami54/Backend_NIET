from django.contrib import admin
from django.utils.html import format_html
from website.models import *


def image_preview(obj, field_name):
    file = getattr(obj, field_name)
    if file:
        return format_html('<img src="{}" width="60" height="60" style="object-fit:contain;" />', file.url)
    return "No Image"

def file_preview(obj, field_name):
    file = getattr(obj, field_name)
    if file:
        return format_html('<a href="{}" target="_blank">Open</a>', file.url)
    return "None"



@admin.register(AboutCollege)
class AboutCollegeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "short_name", "logo_preview", "is_active", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("full_name", "short_name", "email_address", "telephone")
    readonly_fields = ("created_at", "updated_at")

    def logo_preview(self, obj):
        return image_preview(obj, "logo")
    logo_preview.short_description = "Logo"

    fieldsets = (
        ("Basic Information", {
            "fields": ("full_name", "short_name", "about_text", "brochure")
        }),
        ("Legal & Affiliation", {
            "fields": ("affiliation", "registration")
        }),
        ("Contact Information", {
            "fields": ("address", "post_box", "telephone", "email_address", "google_map")
        }),
        ("Social Links", {
            "fields": ("facebook", "twitter", "instagram", "linkedin")
        }),
        ("Logo", {
            "fields": ("logo",)
        }),
        ("System Info", {
            "fields": ("is_active", "created_at", "updated_at")
        }),
    )

@admin.register(AccreditionAndPartnerShip)
class AccreditionAndPartnerShipAdmin(admin.ModelAdmin):
    list_display = ("heading", "order_priority", "icon_preview")
    ordering = ("order_priority",)
    search_fields = ("heading",)
    
    def icon_preview(self, obj):
        return image_preview(obj, "icon")
    icon_preview.short_description = "Icon"


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("page_name", "heading_line", "background_preview")
    search_fields = ("page_name", "heading_line")
    list_filter = ("page_name",)

    def background_preview(self, obj):
        return image_preview(obj, "background_image")
    background_preview.short_description = "Background Image"

    fieldsets = (
        ("Page Info", {
            "fields": ("page_name", "heading_line", "support_text")
        }),
        ("Background Image", {
            "fields": ("background_image",)
        }),
        ("CTA Buttons", {
            "fields": (
                "call_to_action_1", "call_to_action_2", "call_to_action_3",
                "call_to_action_4", "call_to_action_5", "call_to_action_6",
                "call_to_action_7"
            )
        }),
    )

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ("intake_year", "heading_line", "deadline")
    search_fields = ("intake_year", "heading_line", "deadline")


@admin.register(AdmissionStep)
class AdmissionStepAdmin(admin.ModelAdmin):
    list_display = ("heading", "order_priority", "admission", "icon_preview")
    ordering = ("order_priority",)
    search_fields = ("heading", "admission__heading_line")

    def icon_preview(self, obj):
        return image_preview(obj, "icon")
    icon_preview.short_description = "Icon"


@admin.register(WhySection)
class WhySectionAdmin(admin.ModelAdmin):
    list_display = ("heading_line", "support_text")
    search_fields = ("heading_line",)


@admin.register(WhySectionContent)
class WhySectionContentAdmin(admin.ModelAdmin):
    list_display = ("heading", "why_section", "order_priority", "icon_preview", "photo_preview")
    ordering = ("order_priority",)
    search_fields = ("heading", "why_section__heading_line")

    def icon_preview(self, obj):
        return image_preview(obj, "icon")

    def photo_preview(self, obj):
        return image_preview(obj, "photo")

    icon_preview.short_description = "Icon"
    photo_preview.short_description = "Photo"


@admin.register(LifeSection)
class LifeSectionAdmin(admin.ModelAdmin):
    list_display = ("heading_line", "support_text", "video_file")
    search_fields = ("heading_line",)


@admin.register(LifeSectionContent)
class LifeSectionContentAdmin(admin.ModelAdmin):
    list_display = ("heading", "life_section", "order_priority", "icon_preview")
    ordering = ("order_priority",)

    def icon_preview(self, obj):
        return image_preview(obj, "icon")
    icon_preview.short_description = "Icon"


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "profession", "photo_preview")
    search_fields = ("name", "profession")

    def photo_preview(self, obj):
        return image_preview(obj, "photo")
    photo_preview.short_description = "Photo"


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ("question_text",)
    search_fields = ("question_text", "answer_text")


@admin.register(HomePageAccreditionAndPartnerShip)
class HomePageAccreditionAndPartnerShipAdmin(admin.ModelAdmin):
    list_display = ("accredition",)
    search_fields = ("accredition__heading",)
    list_filter = ("accredition",)

# about us 
@admin.register(EmploymentProvider)
class EmploymentProviderAdmin(admin.ModelAdmin):
    list_display = ("employment_by",)
    search_fields = ("employment_by",)


@admin.register(EmploymentProviderName)
class EmploymentProviderNameAdmin(admin.ModelAdmin):
    list_display = ("name", "employment_provider")
    search_fields = ("name", "employment_provider__employment_by")
    list_filter = ("employment_provider",)


@admin.register(AboutUsWhySection)
class AboutUsWhySectionAdmin(admin.ModelAdmin):
    list_display = ("heading_line", "support_text")
    search_fields = ("heading_line",)


@admin.register(AboutUsWhySectionContent)
class AboutUsWhySectionContentAdmin(admin.ModelAdmin):
    list_display = ("heading", "aboutus_why", "order_priority", "icon_preview")
    ordering = ("order_priority",)
    search_fields = ("heading", "aboutus_why__heading_line")

    def icon_preview(self, obj):
        return image_preview(obj, "icon")
    icon_preview.short_description = "Icon"


@admin.register(AboutUsTimeline)
class AboutUsTimelineAdmin(admin.ModelAdmin):
    list_display = ("heading_line", "support_text")
    search_fields = ("heading_line",)


@admin.register(AboutUsTimelineContent)
class AboutUsTimelineContentAdmin(admin.ModelAdmin):
    list_display = ("year", "heading", "aboutus_timeline", "order_priority", "icon_preview")
    ordering = ("order_priority",)
    search_fields = ("year", "heading", "aboutus_timeline__heading_line")

    def icon_preview(self, obj):
        return image_preview(obj, "icon")
    icon_preview.short_description = "Icon"


@admin.register(AboutPageAccreditionAndPartnerShip)
class AboutPageAccreditionAndPartnerShipAdmin(admin.ModelAdmin):
    list_display = ("accredition",)
    search_fields = ("accredition__heading",)
    list_filter = ("accredition",)

# academic 

@admin.register(AcademicPrograms)
class AcademicProgramsAdmin(admin.ModelAdmin):
    list_display = ("full_name", "duration", "credit", "current_intake", "total_seats", "slug", "brochure_preview")
    search_fields = ("full_name", "slogan", "about_program")
    prepopulated_fields = {"slug": ("full_name",)}

    def brochure_preview(self, obj):
        return file_preview(obj, "brochure")
    brochure_preview.short_description = "Brochure"


@admin.register(AcademicProgramObjectives)
class AcademicProgramObjectivesAdmin(admin.ModelAdmin):
    list_display = ("program", "objective_text")
    list_filter = ("program",)
    search_fields = ("objective_text", "program__full_name")


@admin.register(WhyAcademicProgram)
class WhyAcademicProgramAdmin(admin.ModelAdmin):
    list_display = ("program", "why_text")
    list_filter = ("program",)
    search_fields = ("why_text", "program__full_name")


@admin.register(AcademicProgramCareerProspect)
class AcademicProgramCareerProspectAdmin(admin.ModelAdmin):
    list_display = ("program", "career_text")
    list_filter = ("program",)
    search_fields = ("career_text",)


@admin.register(AcademicProgramKeySkills)
class AcademicProgramKeySkillsAdmin(admin.ModelAdmin):
    list_display = ("program", "skill_text")
    list_filter = ("program",)
    search_fields = ("skill_text",)


@admin.register(AcademicProgramEligibility)
class AcademicProgramEligibilityAdmin(admin.ModelAdmin):
    list_display = ("program", "eligibility_text")
    list_filter = ("program",)
    search_fields = ("eligibility_text",)


@admin.register(AcademicProgramEntranceExamInfo)
class AcademicProgramEntranceExamInfoAdmin(admin.ModelAdmin):
    list_display = ("program", "entrance_text")
    list_filter = ("program",)
    search_fields = ("entrance_text",)


@admin.register(AcademicProgramScholarship)
class AcademicProgramScholarshipAdmin(admin.ModelAdmin):
    list_display = ("program", "scholarship_text")
    list_filter = ("program",)
    search_fields = ("scholarship_text",)


@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(AcademicSemester)
class AcademicSemesterAdmin(admin.ModelAdmin):
    list_display = ("name", "total_credit")
    search_fields = ("name",)


@admin.register(AcademicFeeStructure)
class AcademicFeeStructureAdmin(admin.ModelAdmin):
    list_display = ("program", "year", "fee_name", "fee_amount", )
    list_filter = ("program", "year")
    search_fields = ("fee_name", "program__full_name")





@admin.register(LabResourceContent)
class LabResourceContentAdmin(admin.ModelAdmin):
    list_display = ("heading",  "order_priority", "icon_preview")
    ordering = ("order_priority",)
    search_fields = ("heading",)

    def icon_preview(self, obj):
        return image_preview(obj, "icon")
    icon_preview.short_description = "Icon"

@admin.register(LabResourceFeatures)
class LabResourceFeaturesAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(AcademicProgramLabResource)
class AcademicProgramLabResourceAdmin(admin.ModelAdmin):
    list_display = ("program", )
    list_filter = ("program",)
    search_fields = ("program",)


@admin.register(AcademicIndustryPartnershipContent)
class AcademicIndustryPartnershipContentAdmin(admin.ModelAdmin):
    list_display = ("heading", "order_priority", "icon_preview")
    ordering = ("order_priority",)
    search_fields = ("heading",)

    def icon_preview(self, obj):
        return image_preview(obj, "icon")
    icon_preview.short_description = "Icon"


@admin.register(AcademicIndustryPartnership)
class AcademicIndustryPartnershipAdmin(admin.ModelAdmin):
    list_display = ("program", "content")
    list_filter = ("program",)
    search_fields = ("content__heading",)


@admin.register(AcademicCurriculum)
class AcademicCurriculumAdmin(admin.ModelAdmin):
    list_display = ("heading", "program", "program_structure_preview", "syllabus_preview")
    search_fields = ("heading", "program__full_name")

    def program_structure_preview(self, obj):
        return file_preview(obj, "program_structure")
    program_structure_preview.short_description = "Structure"

    def syllabus_preview(self, obj):
        return file_preview(obj, "syllabus")
    syllabus_preview.short_description = "Syllabus"


@admin.register(AcademicCourse)
class AcademicCourseAdmin(admin.ModelAdmin):
    list_display = ("program", "year", "semester", "course_name", "course_code", "icon_preview")
    list_filter = ("program", "year", "semester")
    search_fields = ("course_name", "course_code")
    
    def icon_preview(self, obj):
        return image_preview(obj, "icon")
    icon_preview.short_description = "Icon"


@admin.register(ProgramFaq)
class ProgramFaqAdmin(admin.ModelAdmin):
    list_display = ("program", "question_text")
    search_fields = ("question_text", "program__full_name")
    list_filter = ("program",)

# faculty 
@admin.register(FacultyType)
class FacultyTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(FacultyCategories)
class FacultyCategoriesAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(FacultyExpertise)
class FacultyExpertiseAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(FacultyDegree)
class FacultyDegreeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(FacultyDesignation)
class FacultyDesignationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(AcademicFaculty)
class AcademicFacultyAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "phone",
        "faculty_type",
        "faculty_designation",
        "faculty_program",
        "faculty_expertise",
        "faculty_degree",
    )
    search_fields = ("full_name", "email", "phone")
    list_filter = (
        "faculty_type",
        "faculty_designation",
        "faculty_program",
        "faculty_expertise",
        "faculty_degree",
    )
    ordering = ("full_name",)


@admin.register(FacultyAssignedCourse)
class FacultyAssignedCourseAdmin(admin.ModelAdmin):
    list_display = ("faculty", "assigned_course")
    search_fields = ("faculty__full_name", "assigned_course__name")
    list_filter = ("assigned_course", "faculty")
    ordering = ("faculty",)

