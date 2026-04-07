from rest_framework import viewsets

from .serializers import CourseSerializer, LessonSerializer
from .models import Course, Lesson
class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset=Lesson.objects.all()
    serializer_class=LessonSerializer
