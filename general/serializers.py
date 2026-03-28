from rest_framework import serializers
from general.models import *
from student_management.models import Teacher

# Serializers

class CoverImageSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = CoverImage
        fields = "__all__"

    def get_photo_url(self, obj):
        return obj.photo.url if obj.photo else None


class ModalImageSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = ModalImage
        fields = "__all__"

    def get_photo_url(self, obj):
        return obj.photo.url if obj.photo else None


class SliderHomeSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = SliderHome
        fields = "__all__"

    def get_photo_url(self, obj):
        return obj.photo.url if obj.photo else None

class FeatureSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Feature
        fields = "__all__"

    def get_img_url(self, obj):
        return obj.feature_img.url if obj.feature_img else None


class AboutUsSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    about_image_url = serializers.SerializerMethodField()

    class Meta:
        model = AboutUs
        fields = "__all__"

    def get_logo_url(self, obj):
        return obj.logo.url if obj.logo else None

    def get_about_image_url(self, obj):
        return obj.about_image.url if obj.about_image else None

class BoardMembersSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = BoardMembers
        fields = "__all__"

    def get_photo_url(self, obj):
        return obj.photo.url if obj.photo else None


class StaffTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffType
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    staff_type = StaffTypeSerializer()

    class Meta:
        model = Staff
        fields = "__all__"

    def get_photo_url(self, obj):
        return obj.photo.url if obj.photo else None


class CollegeChairmanSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = CollegeChairman
        fields = "__all__"

    def get_photo_url(self, obj):
        return obj.photo.url if obj.photo else None


class SyllabusSerializer(serializers.ModelSerializer):
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model = Syllabus
        fields = "__all__"

    def get_pdf_url(self, obj):
        return obj.pdf.url if obj.pdf else None


class EntranceSyllabusSerializer(serializers.ModelSerializer):
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model = EntranceSyllabus
        fields = "__all__"

    def get_pdf_url(self, obj):
        return obj.pdf.url if obj.pdf else None


class EligiblityCriteriaSerializer(serializers.ModelSerializer):
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model = EligiblityCriteria
        fields = "__all__"

    def get_pdf_url(self, obj):
        return obj.pdf.url if obj.pdf else None

class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = "__all__"

    def get_photo_url(self, obj):
        return obj.photo.url if obj.photo else None

    def get_pdf_url(self, obj):
        return obj.pdf.url if obj.pdf else None


class VaccancySerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model = Vaccancy
        fields = "__all__"

    def get_photo_url(self, obj):
        return obj.photo.url if obj.photo else None

    def get_pdf_url(self, obj):
        return obj.pdf.url if obj.pdf else None


class NoticeSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model = Notice
        fields = "__all__"

    def get_photo_url(self, obj):
        return obj.photo.url if obj.photo else None

    def get_pdf_url(self, obj):
        return obj.pdf.url if obj.pdf else None


class ResultSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    pdf_url = serializers.SerializerMethodField()

    class Meta:
        model = Result
        fields = "__all__"

    def get_photo_url(self, obj):
        return obj.photo.url if obj.photo else None

    def get_pdf_url(self, obj):
        return obj.pdf.url if obj.pdf else None

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = "__all__"

    def get_photo_url(self, obj):
        return obj.photo.url if obj.photo else None

class TestimonialSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial
        fields = "__all__"

    def get_photo_url(self, obj):
        return obj.photo.url if obj.photo else None


class VideoTestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoTestimonial
        fields = "__all__"

class AlumniSerializer(serializers.ModelSerializer):
    profile_picture_url = serializers.SerializerMethodField()

    class Meta:
        model = Alumni
        fields = "__all__"

    def get_profile_picture_url(self, obj):
        return obj.profile_picture.url if obj.profile_picture else None


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    head_of_department = TeacherSerializer()
    syllabus = SyllabusSerializer()

    class Meta:
        model = Department
        fields = "__all__"


class DepartmentTeachersSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = DepartmentTeachers
        fields = "__all__"


class DepartmentGallerySerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    gallery = GallerySerializer()

    class Meta:
        model = DepartmentGallery
        fields = "__all__"


class DepartmentAlumniSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    alumni = AlumniSerializer()

    class Meta:
        model = DepartmentAlumni
        fields = "__all__"


