from rest_framework import serializers

from user_app.models import Instructor

from .models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.StringRelatedField(read_only=True)
    instructor_id = serializers.PrimaryKeyRelatedField(
        source="instructor",
        queryset=Instructor.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
    )

    class Meta:
        model=Course
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "status",
            "price",
            "created_at",
            "updated_at",
            "instructor",
            "instructor_id",
        ]
        #fields=['id','title','slug']

class LessonSerializer(serializers.ModelSerializer):
    course_id = serializers.PrimaryKeyRelatedField(
        source="course",
        queryset=Course.objects.all(),
        write_only=True,
    )
    course = serializers.StringRelatedField(read_only=True)

    class Meta:
        model=Lesson
        fields = [
            "id",
            "title",
            "description",
            "video_url",
            "duration",
            "order",
            "content",
            "created_at",
            "course",
            "course_id",
        ]