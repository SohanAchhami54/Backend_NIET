from django.shortcuts import render
from general.models import *
from general.serializers import *

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def home(request):
    about_infos = AboutUs.objects.filter(is_active=True)
    home_image = HomeImages.objects.last()
    about = AboutUs.objects.last()
    video = HomeVideo.objects.last()
    homeinfo = Home.objects.last()
    features = homeinfo.features.all()
    galleries = Gallery.objects.all()
    galleries_footer = list(Gallery.objects.all())[:4]
    newscontents = News.objects.filter(is_active=True)
    partners = MissionPartners.objects.all()
    sliders = SliderHome.objects.all()
    context_dict = {
        'about_infos':about_infos,
        'home_image':home_image,
        'about':about,
        'video':video,
        'newscontents':newscontents,
        'home_info':homeinfo,
        'features':features,
        'galleries':galleries,
        'galleries_footer':galleries_footer,
        'partners':partners,
        'sliders':sliders,
    }
    return render(request,'page/index.html',context_dict)

def get_gallery(request):

    about = AboutUs.objects.last()
    galleries = Gallery.objects.all()
    galleries_footer = list(Gallery.objects.all())[:4]
    context_dict = {
        'about':about,
        'galleries':galleries,
        'galleries_footer':galleries_footer
    }
    return render(request,'page/gallery.html',context_dict)

def aboutus(request):
    about = AboutUs.objects.last()
    chairman = Chairman.objects.last()
    galleries_footer = list(Gallery.objects.all())[:4]
    context_dict = {
        'about':about,
        'chairman':chairman,
        'galleries_footer':galleries_footer
    }
    return render(request,'page/aboutus.html',context_dict)

def get_chairman_message(request):
    chairman = Chairman.objects.last()
    about = AboutUs.objects.last()
    galleries_footer = list(Gallery.objects.all())[:4]
    context_dict = {'chairman':chairman,'about':about,'galleries_footer':galleries_footer}
    return render(request,'page/chairman_message.html',context_dict)

def get_faculties(request):
    about = AboutUs.objects.last()
    ft = FacultyType.objects.get(type_name="full time")
    fulltime_faculties = Faculty.objects.filter(faculty_type=ft)
    ft = FacultyType.objects.get(type_name="visiting")
    visiting_faculties = Faculty.objects.filter(faculty_type=ft)
    galleries_footer = list(Gallery.objects.all())[:4]
    context_dict = {
        'ff':fulltime_faculties,
        'vf':visiting_faculties,
        'about':about,
        'galleries_footer':galleries_footer
    }
    return render(request,'page/staff.html',context_dict)

def get_syllabus(request):
    about = AboutUs.objects.last()
    galleries_footer = list(Gallery.objects.all())[:4]
    syllabus = Syllabus.objects.last()
    context_dict = {
        'about':about,
        'galleries_footer':galleries_footer,
        'syllabus':syllabus
    }
    return render(request,'page/syllabus.html',context_dict)

def get_news(request):
    newscontents = News.objects.filter(is_active=True)
    about = AboutUs.objects.last()
    galleries_footer = list(Gallery.objects.all())[:4]
    context_dict = {
        'about':about,
        'newscontents':newscontents,
        'galleries_footer':galleries_footer
    }
    return render(request,'page/news.html',context_dict)

def get_vaccancy(request):
    vaccancies = Vaccancy.objects.filter(is_active=True)
    about = AboutUs.objects.last()
    context_dict = {
        'about':about,
        'vaccancies':vaccancies
    }
    return render(request,'page/vaccancy.html',context_dict)

def get_vaccancy_detail(request,slug):
    vaccancies = Vaccancy.objects.filter(is_active=True,slug=slug)
    about = AboutUs.objects.last()
    context_dict = {
        'about':about,
        'vaccancies':vaccancies
    }
    return render(request,'page/vaccancy_detail.html',context_dict)

#news detail
def get_news_detail(request,slug):
    results = News.objects.filter(is_active=True,slug=slug)
    about = AboutUs.objects.last()
    context_dict = {
        'about':about,
        'results':results
    }
    return render(request,'page/news_detail.html',context_dict)

# notice and results 
def get_notice(request):
    results = Notice.objects.filter(is_active=True)
    about = AboutUs.objects.last()
    context_dict = {
        'about':about,
        'results':results
    }
    return render(request,'page/notice.html',context_dict)

def get_notice_detail(request,slug):
    results = Notice.objects.filter(is_active=True,slug=slug)
    about = AboutUs.objects.last()
    context_dict = {
        'about':about,
        'results':results
    }
    return render(request,'page/notice_detail.html',context_dict)

# views for result 
def get_result(request):
    results = Result.objects.filter(is_active=True)
    about = AboutUs.objects.last()
    context_dict = {
        'about':about,
        'results':results
    }
    return render(request,'page/result.html',context_dict)

def get_result_detail(request,slug):
    results = Result.objects.filter(is_active=True,slug=slug)
    about = AboutUs.objects.last()
    context_dict = {
        'about':about,
        'results':results
    }
    return render(request,'page/result_detail.html',context_dict)

# entrance syllabus 
def get_entrance_syllabus(request):
    results = EntranceSyllabus.objects.filter(is_active=True)
    about = AboutUs.objects.last()
    context_dict = {
        'about':about,
        'results':results
    }
    return render(request,'page/entrance.html',context_dict)

def get_entrance_syllabus_detail(request,slug):
    results = EntranceSyllabus.objects.filter(is_active=True,slug=slug)
    about = AboutUs.objects.last()
    context_dict = {
        'about':about,
        'results':results
    }
    return render(request,'page/entrance_detail.html',context_dict)

# eligiblity criteria 
def get_eligiblity_criteria(request):
    results = EligiblityCriteria.objects.filter(is_active=True)
    about = AboutUs.objects.last()
    context_dict = {
        'about':about,
        'results':results
    }
    return render(request,'page/eligiblity.html',context_dict)

def get_eligiblity_criteria_detail(request,slug):
    results = EligiblityCriteria.objects.filter(is_active=True,slug=slug)
    about = AboutUs.objects.last()
    context_dict = {
        'about':about,
        'results':results
    }
    return render(request,'page/eligiblity_detail.html',context_dict)

# staff list

def get_staff(request):
    about = AboutUs.objects.last()
    ft = FacultyType.objects.get(type_name="non-teaching")
    staffs = Faculty.objects.filter(faculty_type=ft)
    galleries_footer = list(Gallery.objects.all())[:4]
    context_dict = {
        'ff':staffs,
        'about':about,
        'galleries_footer':galleries_footer
    }
    return render(request,'page/nonstaff.html',context_dict)




def contact_us(request):
    about = AboutUs.objects.last()
    galleries_footer = list(Gallery.objects.all())[:4]
    context_dict = {
        'about':about,
        'galleries_footer':galleries_footer
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








        
