from rest_framework import serializers
from .models import Instructor, Student
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        exclude = ["password"]

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Instructor
        exclude = ["password"]