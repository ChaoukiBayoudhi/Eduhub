from rest_framework import viewsets

from .serializers import CourseSerializer, LessonSerializer
from .models import Course, Lesson
#CouseViewset is a viewset that allows us to create, read, update and delete courses
#it overrides 6 methods : list(), retrieve(), create(), update(), partial_update(), destroy()
class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    #1st case : using request_params
    #request_params is a dictionary that contains the parameters passed to the API endpoint
    #to get the value of a parameter, we use request.query_params.get(param_name)
    #or we can use request.query_params[param_name]
    def get_published_by_price(self, request):
        pass

class LessonViewSet(viewsets.ModelViewSet):
    queryset=Lesson.objects.all()
    serializer_class=LessonSerializer
