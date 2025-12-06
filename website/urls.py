from django.urls import path
from website import views
 


app_name = "website"
urlpatterns = [
    # for home page 
    path("about/college/",views.AboutCollegeList.as_view(),name="about-college"),
    path('acc/partnership/',views.AccreditionAndPartnerShipList.as_view(),name="acc-partnership-list"),
    path('hero-section/',views.HeroSectionList.as_view(),name='hero-section-list'),
    path('journey-to-niet/',views.AdmissionDetail.as_view(),name='admission-detail'),
    path('journey-to-niet/step/',views.AdmissionStepDetail.as_view(),name='admission-step-detail'),
    path('homepage-accredition-partnership/',views.HomePageAccreditionAndPartnerShipDetail.as_view(),name='HomePage- Accredition-And-PartnerShip-Detail'),
    path('why-graduate-trust-niet/',views.WhySectionDetail.as_view(),name='why-section-detail'),
    path('why-graduate-trust-niet/content/',views.WhySectionContentDetail.as_view(),name='why-section-content-detail'),
    path('experience-niet-life/',views.LifeSectionDetail.as_view(),name='life-section-detail'),
    path('experience-niet-life/content/',views.LifeSectionContentDetail.as_view(),name='life-section-content-detail'),
    path('what-our-students-say/',views.TestimonialList.as_view(),name='testimonial-list'),
    path('got-questions-we-got-answers/',views.FaqList.as_view(),name='faq-list'),
    # for about page 
    path('our-graduates-works-at/',views.EmploymentProviderList.as_view(),name='emplyment-provider-list'),
    path('our-graduates-works-at/name/',views.EmploymentProviderNameDetail.as_view(),name='employment-provider-name-detail'),
    path('why-we-exist/',views.AboutUsWhySectionDetail.as_view(),name='AboutUs-Why-Section-Detail'),
    path('why-we-exist/content/',views.AboutUsWhySectionContentDetail.as_view(),name='AboutUs-Why-Section-ContentDetail'),
    path('journey-timeline/',views.AboutUsTimelineDetail.as_view(),name='AboutUsTimelineDetail'),
    path('journey-timeline/content/',views.AboutUsTimelineContentDetail.as_view(),name='AboutUsTimelineContentDetail'),
    path('aboutus-accredition-partnership/',views.AboutPageAccreditionAndPartnerShipDetail.as_view(),name='AboutPage- Accredition-And-PartnerShip-Detail'),
    # academic program 
    path("academic-programs/",views.AcademicProgramsList.as_view(),name='academic-program-list'),
    path("academic-program/<slug:slug>/",views.AcademicProgramsDetail.as_view(),name='academic-program-detail'),
    # path("what-you-will-learn/",views.AcademicProgramObjectivesDetail.as_view(),name='Academic-Program-Objectives-Detail'),
    # path('why-btech-in-program/',views.WhyAcademicProgramDetail.as_view(),name='Why-Academic-Program-Detail'),
    # path('program-career-prospects/',views.AcademicProgramCareerProspectDetail.as_view(),name='Academic-Program-Career-ProspectDetail'),
    # path('program-key-skills/',views.AcademicProgramKeySkillstDetail.as_view(),name='Academic-ProgramKeySkillst-Detail'),
    # path("program-eligiblity/",views.AcademicProgramEligibilityDetail.as_view(),name='AcademicProgram-Eligibility-Detail'),
    # path("program-entrance-exam/",views.AcademicProgramEntranceExamInfoDetail.as_view(),name='AcademicProgram-EntranceExamInfo-Detail'),
    # path("program-scholarship/",views.AcademicProgramScholarshipDetail.as_view(),name='AcademicProgram-Scholarship-Detail'),
    # path('program-fee-structure/',views.AcademicFeeStructureDetail.as_view(),name='AcademicFee-Structure-Detail'),
    # path('program-lab-resource/',views.LabResourceContentList.as_view(),name='LabResourceContentList'),
    # path('program-lab-resource/features/<int:id>/',views.LabResourceFeaturesDetail.as_view(),name='LabResourceFeaturesDetail'),



]