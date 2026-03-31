from rest_framework import serializers
from .models import Course, Lesson
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
        #fields=['id','title','slug']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lesson
        fields='__all__'