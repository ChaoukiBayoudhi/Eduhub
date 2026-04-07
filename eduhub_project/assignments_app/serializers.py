from rest_framework import serializers

from course_app.models import Lesson
from user_app.models import Student

from .models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    lesson = serializers.StringRelatedField(read_only=True)
    lesson_id = serializers.PrimaryKeyRelatedField(
        source="lesson",
        queryset=Lesson.objects.all(),
        write_only=True,
    )
    student = serializers.StringRelatedField(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        source="student",
        queryset=Student.objects.all(),
        write_only=True,
    )

    class Meta:
        model = Assignment
        fields = [
            "id",
            "lesson",
            "lesson_id",
            "student",
            "student_id",
            "assignment_date",
            "status",
            "created_at",
            "updated_at",
        ]

