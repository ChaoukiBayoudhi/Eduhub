from rest_framework.routers import DefaultRouter

from .views import InstructorViewSet, StudentViewSet

router = DefaultRouter()
router.register("students", StudentViewSet, basename="student")
router.register("instructors", InstructorViewSet, basename="instructor")

urlpatterns = router.urls

