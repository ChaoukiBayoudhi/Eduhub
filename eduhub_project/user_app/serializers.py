from rest_framework import serializers
from .models import Instructor, Student
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Instructor
        fields='__all__'