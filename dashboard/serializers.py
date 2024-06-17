from rest_framework import serializers

from dashboard.models import YearlySchedule,Student,StudentYearlyScheduler
from userprofile.serializers import AppUserSerializer



class YearlyScheduleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = YearlySchedule
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    user = AppUserSerializer(read_only=True)
    class Meta:
        model = Student
        fields = ('id','user','registration_number')

class StudentYearlySchedulerSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)  # Set many=True to handle multiple students
    yearly_schedule = YearlyScheduleSerializer(read_only=True)  # Assuming YearlyScheduleSerializer is defined similarly

    class Meta:
        model = StudentYearlyScheduler
        fields = ('id','student', 'yearly_schedule')

    

