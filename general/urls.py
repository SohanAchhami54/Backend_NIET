from django.urls import path
from general import views


app_name = "general"
urlpatterns = [
    path("",views.home,name='home'),
    path("about/us/",views.aboutus,name="aboutus"),
    path("chairman/message/",views.get_chairman_message,name="chairman_message"),
    path("our/staff/",views.get_faculties,name='get_faculties'),
    path("news/",views.get_news,name='get_news'),
    path('gallery/',views.get_gallery,name='get_gallery'),
    path('vaccancy/',views.get_vaccancy,name='get_vaccancy'),
    path('vaccancy/<slug:slug>/',views.get_vaccancy_detail,name='get_vaccancy'),
    path('notice/',views.get_notice_and_results,name='notice_and_results'),
    path('notice/<slug:slug>/',views.get_notice_and_results_detail,name='notice_and_results_detail'),

    
    path("contact/us/",views.contact_us,name='contact_us'),
    path("handle/message/",views.handle_message,name='handle_message'),

] 