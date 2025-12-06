from website.models import *
from website.serializers import *

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.utils.html import strip_tags


from django.shortcuts import render
from rest_framework.permissions import AllowAny


# Create your views here.
class BaseListView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    model = None
    serializer_class = None

    def get(self, request):
        queryset = self.model.objects.all().order_by('-id')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LastRecordView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    model = None
    serializer_class = None
    def get(self,request):
        queryset = self.model.objects.last()
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BaseDetailView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    base_model = None
    child_model = None
    serializer_class = None
    filter_field = ''
    def get(self,request):
        base_queryset = self.base_model.objects.last()
        filter_kwargs = {self.filter_field: base_queryset}
        child_queryset = self.child_model.objects.filter(**filter_kwargs).order_by("order_priority")
        serializer = self.serializer_class(child_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AboutCollegeList(BaseListView):
    model = AboutCollege
    serializer_class = AboutCollegeSerializer

class AccreditionAndPartnerShipList(BaseListView):
    model = AccreditionAndPartnerShip
    serializer_class = AccreditionAndPartnerShipSerializer

class HeroSectionList(BaseListView):
    model  = HeroSection
    serializer_class = HeroSectionSerializer

class AdmissionDetail(LastRecordView):
    authentication_classes = []
    permission_classes = [AllowAny]
    model = Admission
    serializer_class = AdmissionSerializer

class AdmissionStepDetail(BaseDetailView):
    authentication_classes = []
    permission_classes = [AllowAny]
    base_model = Admission
    child_model = AdmissionStep
    serializer_class = AdmissionStepSerializer
    filter_field = 'admission'

class WhySectionDetail(LastRecordView):
    authentication_classes = []
    permission_classes = [AllowAny]
    model = WhySection
    serializer_class = WhySectionSerializer

class WhySectionContentDetail(BaseDetailView):
    authentication_classes = []
    permission_classes = [AllowAny]
    base_model = WhySection
    child_model = WhySectionContent
    serializer_class = WhySectionContentSerializer
    filter_field = 'why_section'

class LifeSectionDetail(LastRecordView):
    authentication_classes = []
    permission_classes = [AllowAny]
    model = LifeSection
    serializer_class = LifeSectionSerializer

class LifeSectionContentDetail(BaseDetailView):
    authentication_classes = []
    permission_classes = [AllowAny]
    base_model = LifeSection
    child_model = LifeSectionContent
    serializer_class = LifeSectionContentSerializer
    filter_field = 'life_section'

class TestimonialList(BaseListView):
    model  = Testimonial
    serializer_class = TestimonialSerializer

class FaqList(BaseListView):
    model  = Faq
    serializer_class = FaqSerializer

class HomePageAccreditionAndPartnerShipDetail(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    base_model = AccreditionAndPartnerShip
    child_model = HomePageAccreditionAndPartnerShip
    serializer_class = AccreditionAndPartnerShipSerializer
    filter_field = 'accredition'
    def get(self,request):
        child_queryset = self.child_model.objects.all()

        if not child_queryset.exists():
            return Response([], status=status.HTTP_200_OK)
        base_ids = child_queryset.values_list(self.filter_field, flat=True)
        base_queryset = self.base_model.objects.filter(id__in=base_ids).order_by("order_priority")

        serializer = self.serializer_class(base_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EmploymentProviderList(BaseListView):
    model  = Faq
    serializer_class = EmploymentProviderSerializer

class EmploymentProviderNameDetail(BaseDetailView):
    authentication_classes = []
    permission_classes = [AllowAny]
    base_model = EmploymentProvider
    child_model = EmploymentProviderName
    serializer_class = EmploymentProviderNameSerializer
    filter_field = 'employment_provider'

class AboutUsWhySectionDetail(LastRecordView):
    authentication_classes = []
    permission_classes = [AllowAny]
    model = AboutUsWhySection
    serializer_class = AboutUsWhySectionSerializer

class AboutUsWhySectionContentDetail(BaseDetailView):
    authentication_classes = []
    permission_classes = [AllowAny]
    base_model = AboutUsWhySection
    child_model = AboutUsWhySectionContent
    serializer_class = AboutUsWhySectionContentSerializer
    filter_field = 'aboutus_why'


class AboutUsTimelineDetail(LastRecordView):
    authentication_classes = []
    permission_classes = [AllowAny]
    model = AboutUsTimeline
    serializer_class = AboutUsTimelineSerializer

class AboutUsTimelineContentDetail(BaseDetailView):
    authentication_classes = []
    permission_classes = [AllowAny]
    base_model = AboutUsTimeline
    child_model = AboutUsTimelineContent
    serializer_class = AboutUsTimelineContentSerializer
    filter_field = 'aboutus_timeline'

class AboutPageAccreditionAndPartnerShipDetail(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    base_model = AccreditionAndPartnerShip
    child_model = AboutPageAccreditionAndPartnerShip
    serializer_class = AccreditionAndPartnerShipSerializer
    filter_field = 'accredition'
    def get(self,request):
        child_queryset = self.child_model.objects.all()

        if not child_queryset.exists():
            return Response([], status=status.HTTP_200_OK)
        base_ids = child_queryset.values_list(self.filter_field, flat=True)
        base_queryset = self.base_model.objects.filter(id__in=base_ids).order_by("order_priority")

        serializer = self.serializer_class(base_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# academic programs 
class AcademicProgramsList(BaseListView):
    model  = AcademicPrograms
    serializer_class = AcademicProgramsSerializer

class AcademicProgramsDetail(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    model = AcademicPrograms
    def get(self,request,slug):
        obj = self.model.objects.filter(slug=slug)
        serializer = AcademicProgramsSerializer(obj,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AcademicProgramObjectivesDetail(BaseDetailView):
    authentication_classes = []
    permission_classes = [AllowAny]
    base_model = AcademicPrograms
    child_model = AcademicProgramObjectives
    serializer_class = AcademicProgramObjectivesSerializer
    filter_field = 'program'

class WhyAcademicProgramDetail(BaseDetailView):
    authentication_classes = []
    permission_classes = [AllowAny]
    base_model = AcademicPrograms
    child_model = WhyAcademicProgram
    serializer_class = WhyAcademicProgramSerializer
    filter_field = 'program'

class AcademicProgramCareerProspectDetail(BaseDetailView):
    authentication_classes = []
    permission_classes = [AllowAny]
    base_model = AcademicPrograms
    child_model = AcademicProgramCareerProspect
    serializer_class = AcademicProgramCareerProspectSerializer
    filter_field = 'program'

class AcademicProgramKeySkillstDetail(BaseDetailView):
    authentication_classes = []
    permission_classes = [AllowAny]
    base_model = AcademicPrograms
    child_model = AcademicProgramKeySkills
    serializer_class = AcademicProgramKeySkillsSerializer
    filter_field = 'program'

class AcademicProgramEligibilityDetail(BaseDetailView):
    authentication_classes = []
    permission_classes = [AllowAny]
    base_model = AcademicPrograms
    child_model = AcademicProgramEligibility
    serializer_class = AcademicProgramEligibilitySerializer
    filter_field = 'program'

class AcademicProgramEntranceExamInfoDetail(BaseDetailView):
    authentication_classes = []
    permission_classes = [AllowAny]
    base_model = AcademicPrograms
    child_model = AcademicProgramEntranceExamInfo
    serializer_class = AcademicProgramEntranceExamInfoSerializer
    filter_field = 'program'

class AcademicProgramScholarshipDetail(BaseDetailView):
    authentication_classes = []
    permission_classes = [AllowAny]
    base_model = AcademicPrograms
    child_model = AcademicProgramScholarship
    serializer_class = AcademicProgramScholarshipSerializer
    filter_field = 'program'

class AcademicFeeStructureDetail(BaseDetailView):
    authentication_classes = []
    permission_classes = [AllowAny]
    base_model = AcademicPrograms
    child_model = AcademicFeeStructure
    serializer_class = AcademicFeeStructureSerializer
    filter_field = 'program'

class LabResourceContentList(BaseListView):
    model  = LabResourceContent
    serializer_class = LabResourceContentSerializer

class LabResourceFeaturesDetail(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    def get(self,request,id):
        obj = LabResourceContent.objects.filter(id=id)
        features = LabResourceFeatures.objects.filter(lab_resource_content=obj)
        serializer = LabResourceFeaturesSerializer(features,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    


    





























