from rest_framework import serializers

from dashboard.models import YearlyScheduler,Student,StudentYearlyScheduler,Schedule,Subject,SubjectSchedule,TheoryInternalMarks,PracticalInternalMarks
from userprofile.serializers import AppUserSerializer


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class YearlySchedulerSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearlyScheduler
        fields = '__all__'

class YearlySchedulerSerializerDetail(serializers.ModelSerializer):
    schedule = ScheduleSerializer(read_only=True)
    class Meta:
        model = YearlyScheduler
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    user = AppUserSerializer(read_only=True)
    class Meta:
        model = Student
        fields = ('id','user','registration_number')

class StudentYearlySchedulerSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)  # Set many=True to handle multiple students
    yearly_schedule = YearlySchedulerSerializer(read_only=True)  # Assuming YearlyScheduleSerializer is defined similarly

    class Meta:
        model = StudentYearlyScheduler
        fields = ('id','student', 'yearly_schedule')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class SubjectScheduleSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    schedule = ScheduleSerializer(read_only=True)
    class Meta:
        model = SubjectSchedule
        fields = '__all__'

class TheoryInternalMarksSerializer(serializers.ModelSerializer):
    student_yearly_scheduler = StudentYearlySchedulerSerializer(read_only=True)
    subject = SubjectScheduleSerializer(read_only=True)
    class Meta:
        model = TheoryInternalMarks
        fields = '__all__'   

class PracticalInternalMarksSerializer(serializers.ModelSerializer):
    student_yearly_scheduler = StudentYearlySchedulerSerializer(read_only=True)
    subject = SubjectScheduleSerializer(read_only=True)
    class Meta:
        model = PracticalInternalMarks
        fields = '__all__'  


    

