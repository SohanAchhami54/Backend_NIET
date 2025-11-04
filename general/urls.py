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
    path('aboutus/',views.AboutUsList.as_view(),name='aboutus_list'),
    path('slider/',views.SliderHomeList.as_view(),name='slider_images'),
    path('scrollnews/',views.ScrollNewsList.as_view(),name='scroll_news_list'),
    path('gallery/list/',views.GalleryList.as_view(),name='gallery_list'),
] 