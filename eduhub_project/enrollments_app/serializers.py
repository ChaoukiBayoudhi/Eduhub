from rest_framework import serializers

from course_app.models import Course
from user_app.models import Student

from .models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        source="student",
        queryset=Student.objects.all(),
        write_only=True,
    )
    course = serializers.StringRelatedField(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(
        source="course",
        queryset=Course.objects.all(),
        write_only=True,
    )

    class Meta:
        model = Enrollment
        fields = [
            "id",
            "student",
            "student_id",
            "course",
            "course_id",
            "enrollment_date",
            "completion_date",
            "status",
            "created_at",
            "updated_at",
        ]

