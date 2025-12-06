from rest_framework import serializers
from website.models import * 

class AboutCollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCollege
        fields = '__all__'

class AccreditionAndPartnerShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccreditionAndPartnerShip
        fields = '__all__'

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionStep
        fields = '__all__'

class AdmissionStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionStep
        fields = '__all__'

class WhySectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhySection
        fields = '__all__'

class WhySectionContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhySectionContent
        fields = '__all__'

class LifeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeSection
        fields = '__all__'

class LifeSectionContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeSectionContent
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'

class HomePageAccreditionAndPartnerShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageAccreditionAndPartnerShip
        fields = '__all__'

# about page 
class EmploymentProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentProvider
        fields = '__all__'
class EmploymentProviderNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentProviderName
        fields = '__all__'

class AboutUsWhySectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsWhySection
        fields = '__all__'

class AboutUsWhySectionContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsWhySectionContent
        fields = '__all__'

class AboutUsTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsTimeline
        fields = '__all__'

class AboutUsTimelineContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsTimelineContent
        fields = '__all__'

class AboutPageAccreditionAndPartnerShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPageAccreditionAndPartnerShip
        fields = '__all__'

# academic programs 
class AcademicProgramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicPrograms
        fields = '__all__'

class AcademicProgramObjectivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicProgramObjectives
        fields = '__all__'

class WhyAcademicProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyAcademicProgram
        fields = '__all__'

class AcademicProgramCareerProspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicProgramCareerProspect
        fields = '__all__'

class AcademicProgramKeySkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicProgramKeySkills
        fields = '__all__'

class AcademicProgramEligibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicProgramEligibility
        fields = '__all__'


class AcademicProgramEntranceExamInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicProgramEntranceExamInfo
        fields = '__all__'


class AcademicProgramScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicProgramScholarship
        fields = '__all__'

class AcademicFeeStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicFeeStructure
        fields = '__all__'

class AcademicProgramLabResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicProgramLabResource
        fields = '__all__'

class LabResourceContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabResourceContent
        fields = '__all__'

class LabResourceFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabResourceFeatures
        fields = '__all__'














