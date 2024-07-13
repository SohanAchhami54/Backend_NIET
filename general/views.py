from django.shortcuts import render
from general.models import *
from general.serializers import *

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def home(request):
    sliders = SliderHome.objects.all()
    features = Feature.objects.filter(is_active=True)
    about = AboutUs.objects.last()
    galleries = Gallery.objects.order_by('-id')[:4]
    events = News.objects.filter(is_active=True).order_by('-id')
    testimonials = Testimonial.objects.filter(is_active=True).order_by('-id')
    video_testimonials = VideoTestimonial.objects.filter(is_active=True).order_by('-id')
    faqs = Faq.objects.all()
    if(len(events)>=6):
        events = events[:6]
    
    
    if(len(testimonials)>=4):
        testimonials = testimonials[:4]
    context_dict={
        'sliders':sliders,
        'features':features,
        'about':about,
        'galleries':galleries,
        'events':events,
        'testimonials':testimonials,
        'faqs':faqs,
        'video_testimonials':video_testimonials
    }
    return render(request,'page/index.html',context_dict)

def aboutus(request):
    about = AboutUs.objects.last()
    chairman = CollegeChairman.objects.last()
    context_dict = {
        'about':about,
        'chairman':chairman,
    }
    return render(request,'page/aboutus.html',context_dict)


def get_faculties(request):
    ft = StaffType.objects.get(type_name="teaching")
    fulltime_faculties = Staff.objects.filter(staff_type=ft,job_type="1")
    print(fulltime_faculties)

    visiting_faculties = Staff.objects.filter(staff_type=ft,job_type="2")

    context_dict = {
        'ff':fulltime_faculties,
        'vf':visiting_faculties,
    }
    return render(request,'page/staff.html',context_dict)

def get_syllabus(request):
    syllabus = Syllabus.objects.filter(is_active=True)
    print(syllabus)
    context_dict = {
        'syllabus':syllabus
    }
    return render(request,'page/syllabus.html',context_dict)


def get_syllabus_detail(request,slug):
    syllabus = Syllabus.objects.get(slug=slug,is_active=True)
    print(syllabus)
    context_dict = {
        'syllabus':syllabus
    }
    return render(request,'page/syllabus_detail.html',context_dict)

def get_news(request):
    newscontents = News.objects.filter(is_active=True)

    context_dict = {
        'events':newscontents,

    }
    return render(request,'page/news.html',context_dict)

def get_news_detail(request,slug):
    results = News.objects.get(is_active=True,slug=slug)
    context_dict = {
        'result':results
    }
    return render(request,'page/news_detail.html',context_dict)

# notice and results 
def get_notice(request):
    results = Notice.objects.filter(is_active=True).order_by('-id')
    context_dict = {
        'results':results
    }
    return render(request,'page/notice.html',context_dict)

def get_notice_detail(request,slug):
    result = Notice.objects.get(is_active=True,slug=slug)
    context_dict = {
        'result':result
    }
    return render(request,'page/notice_detail.html',context_dict)

# views for result 
def get_result(request):
    results = Result.objects.filter(is_active=True).order_by('-id')
    context_dict = {
        'results':results
    }
    return render(request,'page/result.html',context_dict)

def get_result_detail(request,slug):
    result = Result.objects.get(is_active=True,slug=slug)
    context_dict = {
        'result':result
    }
    return render(request,'page/result_detail.html',context_dict)

def get_vaccancy(request):
    results = Vaccancy.objects.filter(is_active=True).order_by('-id')
    context_dict = {

        'results':results
    }
    return render(request,'page/vaccancy.html',context_dict)

def get_vaccancy_detail(request,slug):
    result = Vaccancy.objects.get(is_active=True,slug=slug)
    context_dict = {
        'result':result
    }
    return render(request,'page/vaccancy_detail.html',context_dict)

# entrance syllabus 
def get_entrance_syllabus(request):
    results = EntranceSyllabus.objects.filter(is_active=True)
    context_dict = {
        'results':results
    }
    return render(request,'page/entrance.html',context_dict)

def get_entrance_syllabus_detail(request,slug):
    results = EntranceSyllabus.objects.get(is_active=True,slug=slug)

    context_dict = {
        'result':results
    }
    return render(request,'page/entrance_detail.html',context_dict)

# eligiblity criteria 
def get_eligiblity_criteria(request):
    results = EligiblityCriteria.objects.filter(is_active=True)
    context_dict = {
        'results':results
    }
    return render(request,'page/eligiblity.html',context_dict)

def get_eligiblity_criteria_detail(request,slug):
    results = EligiblityCriteria.objects.get(is_active=True,slug=slug)
    context_dict = {
        'result':results
    }
    return render(request,'page/eligiblity_detail.html',context_dict)



def get_gallery(request):
    gallery = Gallery.objects.all()
    context_dict = {
        'gallery':gallery,
    }
    return render(request,'page/gallery.html',context_dict)



# def get_chairman_message(request):
#     chairman = Chairman.objects.last()
#     about = AboutUs.objects.last()
#     galleries_footer = list(Gallery.objects.all())[:4]
#     context_dict = {'chairman':chairman,'about':about,'galleries_footer':galleries_footer}
#     return render(request,'page/chairman_message.html',context_dict)

# def get_faculties(request):
#     about = AboutUs.objects.last()
#     ft = FacultyType.objects.get(type_name="full time")
#     fulltime_faculties = Faculty.objects.filter(faculty_type=ft)
#     ft = FacultyType.objects.get(type_name="visiting")
#     visiting_faculties = Faculty.objects.filter(faculty_type=ft)
#     galleries_footer = list(Gallery.objects.all())[:4]
#     context_dict = {
#         'ff':fulltime_faculties,
#         'vf':visiting_faculties,
#         'about':about,
#         'galleries_footer':galleries_footer
#     }
#     return render(request,'page/staff.html',context_dict)

# def get_syllabus(request):
#     about = AboutUs.objects.last()
#     galleries_footer = list(Gallery.objects.all())[:4]
#     syllabus = Syllabus.objects.last()
#     context_dict = {
#         'about':about,
#         'galleries_footer':galleries_footer,
#         'syllabus':syllabus
#     }
#     return render(request,'page/syllabus.html',context_dict)

# def get_news(request):
#     newscontents = News.objects.filter(is_active=True)
#     about = AboutUs.objects.last()
#     galleries_footer = list(Gallery.objects.all())[:4]
#     context_dict = {
#         'about':about,
#         'newscontents':newscontents,
#         'galleries_footer':galleries_footer
#     }
#     return render(request,'page/news.html',context_dict)



# #news detail
# def get_news_detail(request,slug):
#     results = News.objects.filter(is_active=True,slug=slug)
#     about = AboutUs.objects.last()
#     context_dict = {
#         'about':about,
#         'results':results
#     }
#     return render(request,'page/news_detail.html',context_dict)

# # notice and results 
# def get_notice(request):
#     results = Notice.objects.filter(is_active=True)
#     about = AboutUs.objects.last()
#     context_dict = {
#         'about':about,
#         'results':results
#     }
#     return render(request,'page/notice.html',context_dict)

# def get_notice_detail(request,slug):
#     results = Notice.objects.filter(is_active=True,slug=slug)
#     about = AboutUs.objects.last()
#     context_dict = {
#         'about':about,
#         'results':results
#     }
#     return render(request,'page/notice_detail.html',context_dict)





# # staff list

def get_staff(request):
    about = AboutUs.objects.last()
    ft = StaffType.objects.get(type_name="non-teaching")
    staffs = Staff.objects.filter(staff_type=ft)
    context_dict = {
        'ff':staffs,
    }
    return render(request,'page/nonstaff.html',context_dict)




def contact_us(request):
    about = AboutUs.objects.last()
    context_dict = {
        'about':about,
    }
    return render(request,'page/contact.html',context_dict)

from django.http import JsonResponse
def handle_message(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        message = request.POST.get('message')

        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error':False}) 

def get_enquiry(request):
    about = AboutUs.objects.last()
    context_dict = {
        'about':about,
    }
    return render(request,'page/enquiry.html',context_dict)


# drf api view 
class ContactMessageCreate(APIView):
    def post(self, request, format=None):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








        
