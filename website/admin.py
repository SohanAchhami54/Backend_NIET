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
    list_display = ("full_name", "short_name", "affiliation", "telephone", "email_address", "is_active")
    search_fields = ("full_name", "short_name", "affiliation", "email_address")
    list_filter = ("is_active",)
    readonly_fields = ("created_at", "updated_at")
    ordering = ("full_name",)


@admin.register(AccreditionAndPartnerShip)
class AccreditionAndPartnerShipAdmin(admin.ModelAdmin):
    list_display = ("heading", "order_priority")
    search_fields = ("heading",)
    ordering = ("order_priority", "heading")

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("page_name", "heading_line")
    search_fields = ("page_name", "heading_line")
    ordering = ("page_name",)

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ("intake_year", "deadline", "heading_line")
    search_fields = ("intake_year", "heading_line")
    ordering = ("intake_year",)

@admin.register(AdmissionStep)
class AdmissionStepAdmin(admin.ModelAdmin):
    list_display = ("heading", "order_priority", "admission")
    search_fields = ("heading", "admission__heading_line")
    list_filter = ("admission",)
    ordering = ("order_priority",)

@admin.register(WhySection)
class WhySectionAdmin(admin.ModelAdmin):
    list_display = ("heading_line", "support_text")
    search_fields = ("heading_line",)
    ordering = ("heading_line",)

@admin.register(WhySectionContent)
class WhySectionContentAdmin(admin.ModelAdmin):
    list_display = ("heading", "why_section", "order_priority")
    search_fields = ("heading", "why_section__heading_line")
    list_filter = ("why_section",)
    ordering = ("order_priority",)

@admin.register(LifeSection)
class LifeSectionAdmin(admin.ModelAdmin):
    list_display = ("heading_line", "support_text")
    search_fields = ("heading_line",)
    ordering = ("heading_line",)

@admin.register(LifeSectionContent)
class LifeSectionContentAdmin(admin.ModelAdmin):
    list_display = ("heading", "life_section", "order_priority")
    search_fields = ("heading", "life_section__heading_line")
    list_filter = ("life_section",)
    ordering = ("order_priority",)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "profession")
    search_fields = ("name", "profession")
    ordering = ("name",)

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ("question_text",)
    search_fields = ("question_text", "answer_text")
    ordering = ("question_text",)

@admin.register(HomePageAccreditionAndPartnerShip)
class HomePageAccreditionAndPartnerShipAdmin(admin.ModelAdmin):
    list_display = ("accredition",)
    search_fields = ("accredition__heading",)
    ordering = ("accredition",)

@admin.register(EmploymentProvider)
class EmploymentProviderAdmin(admin.ModelAdmin):
    list_display = ("employment_by",)
    search_fields = ("employment_by",)
    ordering = ("employment_by",)

@admin.register(EmploymentProviderName)
class EmploymentProviderNameAdmin(admin.ModelAdmin):
    list_display = ("name", "employment_provider")
    search_fields = ("name", "employment_provider__employment_by")
    list_filter = ("employment_provider",)
    ordering = ("name",)

@admin.register(AboutUsWhySection)
class AboutUsWhySectionAdmin(admin.ModelAdmin):
    list_display = ("heading_line", "support_text")
    search_fields = ("heading_line",)
    ordering = ("heading_line",)

@admin.register(AboutUsWhySectionContent)
class AboutUsWhySectionContentAdmin(admin.ModelAdmin):
    list_display = ("heading", "aboutus_why", "order_priority")
    search_fields = ("heading", "aboutus_why__heading_line")
    list_filter = ("aboutus_why",)
    ordering = ("order_priority",)

@admin.register(AboutUsTimeline)
class AboutUsTimelineAdmin(admin.ModelAdmin):
    list_display = ("heading_line", "support_text")
    search_fields = ("heading_line",)
    ordering = ("heading_line",)

@admin.register(AboutUsTimelineContent)
class AboutUsTimelineContentAdmin(admin.ModelAdmin):
    list_display = ("year", "heading", "aboutus_timeline", "order_priority")
    search_fields = ("heading", "aboutus_timeline__heading_line", "year")
    list_filter = ("aboutus_timeline",)
    ordering = ("order_priority",)

@admin.register(AboutPageAccreditionAndPartnerShip)
class AboutPageAccreditionAndPartnerShipAdmin(admin.ModelAdmin):
    list_display = ("accredition",)
    search_fields = ("accredition__heading",)
    ordering = ("accredition",)

@admin.register(AcademicPrograms)
class AcademicProgramsAdmin(admin.ModelAdmin):
    list_display = ("full_name", "slogan", "duration", "current_intake", "total_seats")
    search_fields = ("full_name", "slogan")
    ordering = ("full_name",)
    prepopulated_fields = {"slug": ("full_name",)}

@admin.register(AcademicProgramObjectives)
class AcademicProgramObjectivesAdmin(admin.ModelAdmin):
    list_display = ("program", "objective_text")
    search_fields = ("program__full_name", "objective_text")
    list_filter = ("program",)
    ordering = ("program",)

@admin.register(WhyAcademicProgram)
class WhyAcademicProgramAdmin(admin.ModelAdmin):
    list_display = ("program", "why_text")
    search_fields = ("program__full_name", "why_text")
    list_filter = ("program",)
    ordering = ("program",)

@admin.register(AcademicProgramCareerProspect)
class AcademicProgramCareerProspectAdmin(admin.ModelAdmin):
    list_display = ("program", "career_text")
    search_fields = ("program__full_name", "career_text")
    list_filter = ("program",)
    ordering = ("program",)

@admin.register(AcademicProgramKeySkills)
class AcademicProgramKeySkillsAdmin(admin.ModelAdmin):
    list_display = ("program", "skill_text")
    search_fields = ("program__full_name", "skill_text")
    list_filter = ("program",)
    ordering = ("program",)

@admin.register(AcademicProgramEligibility)
class AcademicProgramEligibilityAdmin(admin.ModelAdmin):
    list_display = ("program", "eligibility_text")
    search_fields = ("program__full_name", "eligibility_text")
    list_filter = ("program",)
    ordering = ("program",)

@admin.register(AcademicProgramEntranceExamInfo)
class AcademicProgramEntranceExamInfoAdmin(admin.ModelAdmin):
    list_display = ("program", "entrance_text")
    search_fields = ("program__full_name", "entrance_text")
    list_filter = ("program",)
    ordering = ("program",)

@admin.register(AcademicProgramScholarship)
class AcademicProgramScholarshipAdmin(admin.ModelAdmin):
    list_display = ("program", "scholarship_text")
    search_fields = ("program__full_name", "scholarship_text")
    list_filter = ("program",)
    ordering = ("program",)

@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)

@admin.register(AcademicSemester)
class AcademicSemesterAdmin(admin.ModelAdmin):
    list_display = ("name", "total_credit")
    search_fields = ("name",)
    ordering = ("name",)

@admin.register(AcademicFeeStructure)
class AcademicFeeStructureAdmin(admin.ModelAdmin):
    list_display = ("program", "year", "fee_name", "fee_amount")
    search_fields = ("program__full_name", "fee_name")
    list_filter = ("program", "year")
    ordering = ("program", "year")

@admin.register(AcademicProgramLabResource)
class AcademicProgramLabResourceAdmin(admin.ModelAdmin):
    list_display = ("heading", "program")
    search_fields = ("heading", "program__full_name")
    list_filter = ("program",)
    ordering = ("program",)

@admin.register(LabResourceContent)
class LabResourceContentAdmin(admin.ModelAdmin):
    list_display = ("heading", "academic_lab_resource", "order_priority")
    search_fields = ("heading", "academic_lab_resource__heading")
    list_filter = ("academic_lab_resource",)
    ordering = ("order_priority",)

@admin.register(LabResourceFeatures)
class LabResourceFeaturesAdmin(admin.ModelAdmin):
    list_display = ("name", "lab_resource_content")
    search_fields = ("name", "lab_resource_content__heading")
    list_filter = ("lab_resource_content",)
    ordering = ("lab_resource_content",)

@admin.register(AcademicIndustryPartnership)
class AcademicIndustryPartnershipAdmin(admin.ModelAdmin):
    list_display = ("heading", "program")
    search_fields = ("heading", "program__full_name")
    list_filter = ("program",)
    ordering = ("program",)

@admin.register(AcademicIndustryPartnershipContent)
class AcademicIndustryPartnershipContentAdmin(admin.ModelAdmin):
    list_display = ("heading", "partner", "order_priority")
    search_fields = ("heading", "partner__heading")
    list_filter = ("partner",)
    ordering = ("order_priority",)

@admin.register(AcademicCurriculum)
class AcademicCurriculumAdmin(admin.ModelAdmin):
    list_display = ("heading", "program")
    search_fields = ("heading", "program__full_name")
    list_filter = ("program",)
    ordering = ("program",)

@admin.register(AcademicCourse)
class AcademicCourseAdmin(admin.ModelAdmin):
    list_display = ("course_name", "course_code", "program", "year", "semester")
    search_fields = ("course_name", "course_code", "program__full_name")
    list_filter = ("program", "year", "semester")
    ordering = ("program", "year", "semester")



@admin.register(ProgramFaq)
class ProgramFaqAdmin(admin.ModelAdmin):
    list_display = ('program', 'question_text')
    list_filter = ('program',)
    search_fields = ('question_text', 'answer_text')


@admin.register(FacultyType)
class FacultyTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(FacultyCategories)
class FacultyCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(FacultyExpertise)
class FacultyExpertiseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(FacultyDegree)
class FacultyDegreeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(FacultyDesignation)
class FacultyDesignationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(AcademicFaculty)
class AcademicFacultyAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone',
        'faculty_type',
        'faculty_designation',
        'faculty_program',
        'faculty_expertise',
        'faculty_degree',
    )
    list_filter = (
        'faculty_type',
        'faculty_designation',
        'faculty_program',
        'faculty_expertise',
        'faculty_degree',
    )
    search_fields = ('full_name', 'email', 'phone')


@admin.register(FacultyAssignedCourse)
class FacultyAssignedCourseAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'assigned_course')
    list_filter = ('faculty', 'assigned_course')
    search_fields = ('faculty__full_name', 'assigned_course__name')


