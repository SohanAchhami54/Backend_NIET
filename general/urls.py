from django.urls import path
from general import views
 


app_name = "general"
urlpatterns = [
    path("",views.home,name='home'),
    path("about/us/",views.aboutus,name="aboutus"),
    path("our/faculty/",views.get_faculties,name='get_faculties'),
    path("syllabus/",views.get_syllabus,name='get_syllabus'),
    path("syllabus/<slug:slug>/",views.get_syllabus_detail,name='get_syllabus_detail'),
    path("news/",views.get_news,name='get_news'),
    path('news/<slug:slug>/',views.get_news_detail,name='news_detail'),
    path('notice/',views.get_notice,name='notice'),
    path('notice/<slug:slug>/',views.get_notice_detail,name='notice_detail'),
    path('result/',views.get_result,name='result'),
    path('result/<slug:slug>/',views.get_result_detail,name='result_detail'),
    path('vaccancy/',views.get_vaccancy,name='get_vaccancy'),
    path('vaccancy/<slug:slug>/',views.get_vaccancy_detail,name='get_vaccancy'),

    path('entrace/syllabus/',views.get_entrance_syllabus,name='entrance_syllabus'),
    path('entrance/syllabus/<slug:slug>/',views.get_entrance_syllabus_detail,name='entrance_syllabus_detail'),

    path('eligiblity/criteria/',views.get_eligiblity_criteria,name='get_eligiblity_criteria'),
    path('eligiblity/criteria/<slug:slug>/',views.get_eligiblity_criteria_detail,name='get_eligiblity_criteria_detail'),

    path("contact/us/",views.contact_us,name='contact_us'),
    path("enquiry/",views.get_enquiry,name='get_enquiry'),
    path("message/",views.ContactMessageCreate.as_view(),name='handle_message'),

    path('gallery/',views.get_gallery,name='get_gallery'),

    path("our/staff/",views.get_staff,name='get_staffs'),
    path("our/alumni/",views.get_alumni,name='get_alumni'),
    path("alumni/message/<slug:slug>/",views.get_alumni_message,name='get_alumni_message'),

    path('department/<slug:slug>/',views.department_detail,name='department_detail'),

    # path("chairman/message/",views.get_chairman_message,name="chairman_message"),

    # for API
    # path('aboutus/',views.AboutUsList.as_view(),name='aboutus_list'),
    # path('slider/',views.SliderHomeList.as_view(),name='slider_images'),
    # path('scrollnews/',views.ScrollNewsList.as_view(),name='scroll_news_list'),
    # path('gallery/list/',views.GalleryList.as_view(),name='gallery_list'),

    path('api/cover-images/', views.CoverImageList.as_view(), name='cover-image-list'),
    path('api/modal-images/', views.ModalImageList.as_view(), name='modal-image-list'),
    path('api/slider-home/', views.SliderHomeList.as_view(), name='slider-home-list'),
    path('api/features/', views.FeatureList.as_view(), name='feature-list'),
    path('api/about-us/', views.AboutUsList.as_view(), name='about-us-list'),
    path('api/board-members/', views.BoardMembersList.as_view(), name='board-members-list'),
    path('api/staff-types/', views.StaffTypeList.as_view(), name='staff-type-list'),
    path('api/staff/', views.StaffList.as_view(), name='staff-list'),
    path('api/college-chairman/', views.CollegeChairmanList.as_view(), name='college-chairman-list'),
    path('api/syllabus/', views.SyllabusList.as_view(), name='syllabus-list'),
    path('api/entrance-syllabus/', views.EntranceSyllabusList.as_view(), name='entrance-syllabus-list'),
    path('api/eligibility-criteria/', views.EligiblityCriteriaList.as_view(), name='eligibility-criteria-list'),
    path('api/project-categories/', views.ProjectCategoryList.as_view(), name='project-category-list'),
    path('api/news/', views.NewsList.as_view(), name='news-list'),
    path('api/vacancies/', views.VaccancyList.as_view(), name='vacancy-list'),
    path('api/notices/', views.NoticeList.as_view(), name='notice-list'),
    path('api/results/', views.ResultList.as_view(), name='result-list'),
    path('api/contact-messages/', views.ContactMessageList.as_view(), name='contact-message-list'),
    path('api/faqs/', views.FaqList.as_view(), name='faq-list'),
    path('api/gallery/', views.GalleryList.as_view(), name='gallery-list'),
    path('api/testimonials/', views.TestimonialList.as_view(), name='testimonial-list'),
    path('api/video-testimonials/', views.VideoTestimonialList.as_view(), name='video-testimonial-list'),
    path('api/alumni/', views.AlumniList.as_view(), name='alumni-list'),
    path('api/departments/', views.DepartmentList.as_view(), name='department-list'),
    path('api/department-teachers/', views.DepartmentTeachersList.as_view(), name='department-teachers-list'),
    path('api/department-gallery/', views.DepartmentGalleryList.as_view(), name='department-gallery-list'),
    path('api/department-alumni/', views.DepartmentAlumniList.as_view(), name='department-alumni-list'),

    path('api/syllabus/<slug:slug>/',views.SyllabusDetailView.as_view(),name='syllabus-detail-view'),
    path('api/news/<slug:slug>/',views.NewsDetailView.as_view(),name='news-list-details-views'),
    path('api/notice/<slug:slug>/',views.NoticeDetailView.as_view(),name='notice-detail-view'),
    path('api/result/<slug:slug>/',views.ResultDetailView.as_view(),name='result-detail-view'),
    path('api/vaccancy/<slug:slug>/',views.VaccancyDetailView.as_view(),name='vaccancy-detail-view'),
    path('api/entrance-syllabus/<slug:slug>/',views.EntranceSyllabusDetailView.as_view(),name='entrance-syllabus-detail-view'),
    path('api/eligiblity-criteria/<slug:slug>/',views.EligiblityCriteriaDetailView.as_view(),name='eligiblity-detail-view'),
    path('api/alumni-message/<slug:slug>/',views.AlumniDetailView.as_view(),name='alumni-detail-view'),
    path('api/department/<slug:slug>/',views.DepartmentDetailView.as_view(),name='department-detail-view'),
] 