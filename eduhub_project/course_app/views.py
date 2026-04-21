from rest_framework import viewsets, status
from rest_framework.response import Response
from user_app.models import Instructor
from enumerations.enums import CourseStatus
from .serializers import CourseSerializer, LessonSerializer
from .models import Course, Lesson
from rest_framework.decorators import action
from django.db.models import Q

# CouseViewset is a viewset that allows us to create, read, update and delete courses
# it overrides 6 methods : list(), retrieve(), create(), update(), partial_update(), destroy()
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # 1st case : using request_params
    # request_params is a dictionary that contains the parameters passed to the API endpoint
    # to get the value of a parameter, we use request.query_params.get(param_name)
    # or we can use request.query_params[param_name]
    # get Courses published by price
    #by default to call this endpoint, we need to use the following URL:
    # http://localhost:8000/api/courses/published-by-price/?price=100
    # detail=False means that this action is not associated with a specific course
    @action(detail=False, methods=['GET'], url_path='published-by-price')
    def get_published_by_price(self, request):
        # check if the price is provided
        if "price" not in request.query_params:
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data={"error": "Price is required"}
            )
        # get the price
        price = float(request.query_params["price"])
        if price <= 0:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error": "Price must be greater than 0"},
            )
        # get the courses published by price
        courses = Course.objects.filter(status=CourseStatus.PUBLISHED, price__lte=price)
        #or
        #courses =Course.objects.filter(Q(status=CourseStatus.PUBLISHED) & Q(price__lte=price))
        if not courses.exists():
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data={
                    "message": f"No published courses with price less than or equal to {price} found"
                },
            )
        # serialize the courses to convert them to JSON
        # many = True is used to serialize multiple objects (Apply the serializer to each object)
        result = CourseSerializer(courses, many=True)
        return Response(status=status.HTTP_200_OK, data=result.data)

    # 2nd case : using path variables
    # the parth variable is passed as a parameter to the API endpoint
    #get course by instructor given the instructor id
    #by default to call this endpoint, we need to use the following URL:
    # http://localhost:8000/api/courses/instructor/<instructor_id>/
    #instructor id is a uuid type
    # (?P<instructor_id>[0-9a-f-]{36}) is a regex pattern to match the instructor id (uuid format)
    # [0-9a-f-] to specify that the id is composed only by digits and letters (a to f) and the character '-'
    # {36} to specify that the id is 36 characters long
    #?P<instructor_id> is the name of the path variable
    @action(detail=False, methods=['GET'], url_path='instructor/(?P<instructor_id>[0-9a-f-]{36})')
    def get_course_by_instructor(self, request, instructor_id):
        #get courses by instructor given the instructor id
        courses = Course.objects.select_related('instructor').filter(instructor_id=instructor_id)
        #or 
        #instructor = Instructor.objects.get(id=instructor_id)
        #courses = Course.objects.filter(instructor=instructor)
        if not courses.exists():
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data={
                    "message": f"No courses found for instructor with id {instructor_id}"
                },
            )

        #status is by default 200 OK
        return Response(CourseSerializer(courses, many=True).data)
        

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
