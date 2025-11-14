from django.shortcuts import render
from general.models import *
from general.serializers import *

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.utils.html import strip_tags


# Create your views here.
def home(request):
    sliders = SliderHome.objects.all().order_by('order_priority')
    features = Feature.objects.filter(is_active=True)
    about = AboutUs.objects.last()
    modal_images = ModalImage.objects.filter(is_active=True).order_by('-id')
    galleries = Gallery.objects.order_by('-id')[:4]
    events = News.objects.filter(is_active=True).order_by('-id')
    scroller_events = News.objects.filter(is_active=True,scroll=True).order_by('-id')
    for scroll_event in scroller_events:
        scroll_event.content = strip_tags(scroll_event.content)
    
    scroller_notices = Notice.objects.filter(is_active=True,scroll=True).order_by('-id')
    for scroll_notice in scroller_notices:
        scroll_notice.content = strip_tags(scroll_notice.content)
    testimonials = Testimonial.objects.filter(is_active=True).order_by('-id')
    video_testimonials = VideoTestimonial.objects.filter(is_active=True).order_by('-id')
    faqs = Faq.objects.all()
    departments = Department.objects.all()

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
        'video_testimonials':video_testimonials,
        'scroll_events':scroller_events,
        'scroll_notices':scroller_notices,
        'modal_images':modal_images,
        'departments':departments,
    }

    return render(request,'page/index.html',context_dict)

def aboutus(request):
    about = AboutUs.objects.last()
    chairman = CollegeChairman.objects.last()
    members = BoardMembers.objects.all().order_by('order_priority')
    departments = Department.objects.all()
    context_dict = {
        'about':about,
        'chairman':chairman,
        'members':members,
        'departments':departments
    }
    return render(request,'page/aboutus.html',context_dict)


def get_faculties(request):
    ft = StaffType.objects.get(type_name="teaching")
    fulltime_faculties = Staff.objects.filter(staff_type=ft,job_type="1").order_by('order_priority')

    visiting_faculties = Staff.objects.filter(staff_type=ft,job_type="2").order_by('order_priority')
    departments = Department.objects.all()

    context_dict = {
        'ff':fulltime_faculties,
        'vf':visiting_faculties,
        'departments':departments
    }
    return render(request,'page/staff.html',context_dict)

def get_syllabus(request):
    syllabus = Syllabus.objects.filter(is_active=True).order_by('-id')
    departments = Department.objects.all()
    context_dict = {
        'syllabus':syllabus,
        'departments':departments
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
    newscontents = News.objects.filter(is_active=True).order_by('-id')
    departments = Department.objects.all()
    context_dict = {
        'events':newscontents,
        'departments':departments

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
    departments = Department.objects.all()
    context_dict = {
        'results':results,
        'departments':departments
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
    departments = Department.objects.all()
    context_dict = {
        'results':results,
        'departments':departments
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
    departments = Department.objects.all()
    context_dict = {
        'departments':departments,
        'results':results
    }
    return render(request,'page/vaccancy.html',context_dict)

def get_vaccancy_detail(request,slug):
    result = Vaccancy.objects.get(is_active=True,slug=slug)
    departments = Department.objects.all()
    context_dict = {
        'result':result,
        'departments':departments
    }
    return render(request,'page/vaccancy_detail.html',context_dict)

# entrance syllabus 
def get_entrance_syllabus(request):
    results = EntranceSyllabus.objects.filter(is_active=True)
    departments = Department.objects.all()
    context_dict = {
        'results':results,
        'departments':departments
    }
    return render(request,'page/entrance.html',context_dict)

def get_entrance_syllabus_detail(request,slug):
    results = EntranceSyllabus.objects.get(is_active=True,slug=slug)
    departments = Department.objects.all()
    context_dict = {
        'result':results,
        'departments':departments
    }
    return render(request,'page/entrance_detail.html',context_dict)

# eligiblity criteria 
def get_eligiblity_criteria(request):
    results = EligiblityCriteria.objects.filter(is_active=True)
    departments = Department.objects.all()
    context_dict = {
        'results':results,
        'departments':departments
    }
    return render(request,'page/eligiblity.html',context_dict)

def get_eligiblity_criteria_detail(request,slug):
    results = EligiblityCriteria.objects.get(is_active=True,slug=slug)
    departments = Department.objects.all()
    context_dict = {
        'result':results,
        'departments':departments
    }
    return render(request,'page/eligiblity_detail.html',context_dict)



def get_gallery(request):
    gallery = Gallery.objects.all()
    departments = Department.objects.all()
    context_dict = {
        'gallery':gallery,
        'departments':departments
    }
    return render(request,'page/gallery.html',context_dict)

def get_alumni_message(request,slug):
    alumni = Alumni.objects.get(slug=slug)
    departments = Department.objects.all()
    context_dict = {'alumni':alumni,'departments':departments}
    return render(request,'page/alumni_message.html',context_dict)



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
    staffs = Staff.objects.filter(staff_type=ft).order_by('order_priority')
    departments = Department.objects.all()
    context_dict = {
        'ff':staffs,
        'departments':departments
    }
    return render(request,'page/nonstaff.html',context_dict)

def get_alumni(request):
    about = AboutUs.objects.last()
    alumnis = Alumni.objects.all()
    departments = Department.objects.all()
    context_dict = {
        'alumnis':alumnis,
        'departments':departments
    }
    return render(request,'page/alumni.html',context_dict)




def contact_us(request):
    about = AboutUs.objects.last()
    departments = Department.objects.all()
    context_dict = {
        'about':about,
        'departments':departments
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


from django.shortcuts import render, get_object_or_404

def department_detail(request, slug):
    department = get_object_or_404(Department, slug=slug)
    departments = Department.objects.all()
    return render(request, 'page/department_detail.html', {'department': department,'departments':departments})


# drf api view 
class ContactMessageCreate(APIView):
    def post(self, request, format=None):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# for api 
from rest_framework.permissions import AllowAny

# class AboutUsList(APIView):
#     authentication_classes = []  
#     permission_classes = [AllowAny]
#     def get(self,request):
#         object = AboutUs.objects.all()[0]
#         serializer = AboutUsSerializer(object)
#         return Response(serializer.data,status=status.HTTP_200_OK)

# class SliderHomeList(APIView):
#     authentication_classes = []  
#     permission_classes = [AllowAny]
#     def get(self,request):
#         object = SliderHome.objects.all()
#         serializer = SliderHomeSerializer(object,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

# class GalleryList(APIView):
#     authentication_classes = []  
#     permission_classes = [AllowAny]
#     def get(self,request):
#         object = Gallery.objects.all()
#         serializer = GallerySerializer(object,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

# class ScrollNewsList(APIView):
#     authentication_classes = []  
#     permission_classes = [AllowAny]
#     def get(self,request):
#         object = News.objects.all()
#         serializer = NewsSerializer(object,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)


class BaseListView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    model = None
    serializer_class = None

    def get(self, request):
        queryset = self.model.objects.all().order_by('-id')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# -------------------------
#        API Views
# -------------------------

class CoverImageList(BaseListView):
    model = CoverImage
    serializer_class = CoverImageSerializer


class ModalImageList(BaseListView):
    model = ModalImage
    serializer_class = ModalImageSerializer


class SliderHomeList(BaseListView):
    model = SliderHome
    serializer_class = SliderHomeSerializer


class FeatureList(BaseListView):
    model = Feature
    serializer_class = FeatureSerializer


class AboutUsList(BaseListView):
    model = AboutUs
    serializer_class = AboutUsSerializer


class BoardMembersList(BaseListView):
    model = BoardMembers
    serializer_class = BoardMembersSerializer


class StaffTypeList(BaseListView):
    model = StaffType
    serializer_class = StaffTypeSerializer


class StaffList(BaseListView):
    model = Staff
    serializer_class = StaffSerializer


class CollegeChairmanList(BaseListView):
    model = CollegeChairman
    serializer_class = CollegeChairmanSerializer


class SyllabusList(BaseListView):
    model = Syllabus
    serializer_class = SyllabusSerializer


class EntranceSyllabusList(BaseListView):
    model = EntranceSyllabus
    serializer_class = EntranceSyllabusSerializer


class EligiblityCriteriaList(BaseListView):
    model = EligiblityCriteria
    serializer_class = EligiblityCriteriaSerializer


class ProjectCategoryList(BaseListView):
    model = ProjectCategory
    serializer_class = ProjectCategorySerializer


class NewsList(BaseListView):
    model = News
    serializer_class = NewsSerializer


class VaccancyList(BaseListView):
    model = Vaccancy
    serializer_class = VaccancySerializer


class NoticeList(BaseListView):
    model = Notice
    serializer_class = NoticeSerializer


class ResultList(BaseListView):
    model = Result
    serializer_class = ResultSerializer


class ContactMessageList(BaseListView):
    model = ContactMessage
    serializer_class = ContactMessageSerializer


class FaqList(BaseListView):
    model = Faq
    serializer_class = FaqSerializer


class GalleryList(BaseListView):
    model = Gallery
    serializer_class = GallerySerializer


class TestimonialList(BaseListView):
    model = Testimonial
    serializer_class = TestimonialSerializer


class VideoTestimonialList(BaseListView):
    model = VideoTestimonial
    serializer_class = VideoTestimonialSerializer


class AlumniList(BaseListView):
    model = Alumni
    serializer_class = AlumniSerializer


class DepartmentList(BaseListView):
    model = Department
    serializer_class = DepartmentSerializer


class DepartmentTeachersList(BaseListView):
    model = DepartmentTeachers
    serializer_class = DepartmentTeachersSerializer


class DepartmentGalleryList(BaseListView):
    model = DepartmentGallery
    serializer_class = DepartmentGallerySerializer


class DepartmentAlumniList(BaseListView):
    model = DepartmentAlumni
    serializer_class = DepartmentAlumniSerializer

# get model detail 
class BaseDetailView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    model = None
    serializer_class = None

    def get(self, request, slug):
        instance = self.model.objects.filter(slug=slug).first()
        
        if not instance:
            return Response(
                {"detail": "Not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SyllabusDetailView(BaseDetailView):
    model = Syllabus
    serializer_class = SyllabusSerializer

class NewsDetailView(BaseDetailView):
    model = News
    serializer_class = NewsSerializer

class NoticeDetailView(BaseDetailView):
    model = Notice
    serializer_class = NoticeSerializer

class ResultDetailView(BaseDetailView):
    model = Result
    serializer_class = ResultSerializer

class VaccancyDetailView(BaseDetailView):
    model = Vaccancy
    serializer_class = VaccancySerializer

class EntranceSyllabusDetailView(BaseDetailView):
    model = EntranceSyllabus
    serializer_class = EntranceSyllabusSerializer

class EligiblityCriteriaDetailView(BaseDetailView):
    model = EligiblityCriteria
    serializer_class = EligiblityCriteriaSerializer

class AlumniDetailView(BaseDetailView):
    model = Alumni
    serializer_class = AlumniSerializer

class DepartmentDetailView(BaseDetailView):
    model = Department
    serializer_class = DepartmentSerializer






















        
