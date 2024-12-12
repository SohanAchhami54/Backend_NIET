from rest_framework import serializers
from management.models import Semester,Subject,Teacher,SubjectTeacher,BatchSemester,Batch,Student,StudentInSemester,ExamType,ExamSession,StudentSubjectAttendance,StudentInternalExamResult,SubjectInternalExam,Notice

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','first_name','last_name','photo','registration_number']

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'

class ExamTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamType
        fields = '__all__'

class ExamSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamSession
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class SubjectDetailSerializer(serializers.ModelSerializer):
    semester = SemesterSerializer(read_only=True)
    class Meta:
        model = Subject
        fields = ('name','semester',)

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class SubjectTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectTeacher
        fields = '__all__'


class SubjectTeacherDetailSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)  
    subject = SubjectSerializer(read_only=True)  

    class Meta:
        model = SubjectTeacher
        fields = ['teacher', 'subject', 'is_active', 'created_at', 'updated_at']

class DetailSubjectTeacherSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)  
    subject = SubjectDetailSerializer(read_only=True)  

    class Meta:
        model = SubjectTeacher
        fields = ['teacher', 'subject', 'is_active', 'created_at', 'updated_at']

class BatchSemesterDetailSerializer(serializers.ModelSerializer):
    batch = BatchSerializer(read_only=True)  
    semester = SemesterSerializer(read_only=True)  

    class Meta:
        model = BatchSemester
        fields = ['id','batch', 'semester', 'is_active', 'created_at', 'updated_at']

class StudentInSemesterSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    class Meta:
        model = StudentInSemester
        fields = ['student',]

class StudentSubjectAttendanceSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    class Meta:
        model = StudentSubjectAttendance
        fields = ['subject','day','status',]

class StudentSubjectAttendanceDetailSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    student = StudentSerializer(read_only=True)
    class Meta:
        model = StudentSubjectAttendance
        fields = ['student','subject','day','status',]

class SubjectInternalExamSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    exam_type = ExamTypeSerializer(read_only=True)
    class Meta:
        model = SubjectInternalExam
        fields = ('subject','exam_type','full_marks','pass_marks',)



class StudentInternalExamResultSerializer(serializers.ModelSerializer):
    subject_internalexam = SubjectInternalExamSerializer(read_only=True)
    class Meta:
        model = StudentInternalExamResult
        fields = ('subject_internalexam','marks_obtained',)

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


# class StudentSubjectAttendanceSerializer(serializers.ModelSerializer):
#     subject = SubjectSerializer(read_only=True)
#     total_attendance = serializers.SerializerMethodField()
#     present_count = serializers.SerializerMethodField()
#     absent_count = serializers.SerializerMethodField()

#     class Meta:
#         model = StudentSubjectAttendance
#         fields = ['subject', 'day', 'status', 'total_attendance', 'present_count', 'absent_count']

#     def get_total_attendance(self, obj):
#         # Get total attendance for the student's subject
#         student = obj.student
#         subject = obj.subject
#         return StudentSubjectAttendance.objects.filter(student=student, subject=subject).count()

#     def get_present_count(self, obj):
#         # Get count of present (True) attendance for the student's subject
#         student = obj.student
#         subject = obj.subject
#         return StudentSubjectAttendance.objects.filter(student=student, subject=subject, status=True).count()

#     def get_absent_count(self, obj):
#         # Get count of absent (False) attendance for the student's subject
#         student = obj.student
#         subject = obj.subject
#         return StudentSubjectAttendance.objects.filter(student=student, subject=subject, status=False).count()







