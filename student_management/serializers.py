from rest_framework import serializers
from student_management.models import *

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'
    

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class AcademicBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicBatch
        fields = '__all__'

class AcademicSemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicSemester
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AcademicSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicSubject
        fields = '__all__'
        

class StudentViewSerializer(serializers.ModelSerializer):
    semester = serializers.SerializerMethodField()
    batch = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = ('first_name','last_name','registration_number','photo','semester','batch')
    def get_semester(self,obj):
        sem = StudentBatchSemester.objects.get(student__id=obj.id,batch_semester__is_running=True)
        return sem.batch_semester.academic_semester.number
    def get_batch(self,obj):
        sem = StudentBatchSemester.objects.get(student__id=obj.id,batch_semester__is_running=True)
        return sem.batch_semester.degree_batch.academic_batch.year

class ExternalExamTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalExamType
        fields = '__all__'

class StudentRegisterSerializer(serializers.Serializer):
    university = serializers.CharField()
    degree = serializers.CharField()
    academic_batch = serializers.CharField()
    academic_semester = serializers.CharField()
    excel_file = serializers.FileField()

class TeacherRegisterSerializer(serializers.Serializer):
    excel_file = serializers.FileField()

class StudentBatchSemesterBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentBatchSemester
        fields = '__all__'

class StudentBatchSemesterDetailSerializer(serializers.ModelSerializer):
    semester = serializers.SerializerMethodField()
    is_running_semester = serializers.SerializerMethodField()
    class Meta:
        model = StudentBatchSemester
        fields = ('id','student','batch_semester','section','semester','is_running_semester')
    def get_semester(self,obj):
        semester = obj.batch_semester.academic_semester.number
        return semester
    def get_is_running_semester(self,obj):
        is_running = obj.batch_semester.is_running
        return is_running

class StudentBatchSemesterSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    email = serializers.SerializerMethodField()
    class Meta:
        model = StudentBatchSemester
        fields = ('student','email',)
    def get_email(self,obj):
        user_email = obj.student.user.email
        return user_email


class StudentBatchSemesterBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentBatchSemester
        fields = '__all__'


class ExternalExamResultSerializer(serializers.ModelSerializer):
    program = serializers.CharField()
    examination_held_on = serializers.CharField()
    year_semester = serializers.CharField()
    exam_type = serializers.CharField()
    result_published_date = serializers.CharField()
    result_record = serializers.FileField()
    class Meta:
        model = ExternalExamResult
        fields = '__all__'

class ExternalExamResultContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalExamResultContent
        fields = '__all__'

class ExternalExamResultContentDetailSerializer(serializers.ModelSerializer):
    result_meta = ExternalExamResultSerializer()
    class Meta:
        model = ExternalExamResultContent
        fields = '__all__'

class ExternalExamResultScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalExamResultScore
        fields = '__all__'

class ExternalExamResultScoreDetailSerializer(serializers.ModelSerializer):
    external_result_content = ExternalExamResultContentDetailSerializer()
    class Meta:
        model = ExternalExamResultScore
        fields = '__all__'

class BatchSemesterNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchSemesterNotice
        fields = '__all__'


class BatchSemesterNoticeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchSemesterNotice
        fields = ('batch_semester','attachment','messages','title')

class BatchSemesterNoticeDetailSerializer(serializers.ModelSerializer):
    semester = serializers.SerializerMethodField()
    batch = serializers.SerializerMethodField()
    class Meta:
        model = BatchSemesterNotice
        fields = ('id','batch','semester','attachment','messages','title')
    def get_semester(self,obj):
        return obj.batch_semester.academic_semester.number
    def get_batch(self,obj):
        return obj.batch_semester.degree_batch.academic_batch.year

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class TeacherViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        exclude = ('password',)

class SubjectTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectTeacher
        fields = '__all__'

class SubjectAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectAttendance
        fields = '__all__'

class StudentSubjectAttendanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSubjectAttendanceRecord
        fields = '__all__'

class StudentGradeSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGradeSheet
        fields = '__all__'

class StudentGradeSheetUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGradeSheet
        fields = ('student_batch_semester','grade_sheet')

# for internalresult 
class StudentInternalExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInternalExamResult
        fields = '__all__'

class StudentInternalExamResultContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInternalExamResultContent
        fields = '__all__'

class StudentInternalExamResultContentDetailSerializer(serializers.ModelSerializer):
    record = serializers.SerializerMethodField()
    academic_subject = serializers.SerializerMethodField()

    class Meta:
        model = StudentInternalExamResultContent
        fields = ('marks_obtained', 'academic_subject', 'record')

    def get_record(self, obj):
        return obj.student_internalexam_result.record.url.lstrip('/') if obj.student_internalexam_result and obj.student_internalexam_result.record else None

    def get_academic_subject(self, obj):
        return obj.student_internalexam_result.academic_subject.name if obj.student_internalexam_result and obj.student_internalexam_result.academic_subject else None


    

