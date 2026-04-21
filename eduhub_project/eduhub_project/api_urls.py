from rest_framework.routers import DefaultRouter

from course_app.views import CourseViewSet, LessonViewSet
from user_app.views import InstructorViewSet, StudentViewSet
from enrollments_app.views import EnrollmentViewSet
from assignments_app.views import AssignmentViewSet
from django.urls import include, path

router=DefaultRouter()
router.register(r'courses',CourseViewSet)
router.register(r'lessons',LessonViewSet)
router.register(r'instructors',InstructorViewSet)
router.register(r'students',StudentViewSet)
router.register(r'enrollments',EnrollmentViewSet)
router.register(r'assignments',AssignmentViewSet)
urlpatterns=router.urls