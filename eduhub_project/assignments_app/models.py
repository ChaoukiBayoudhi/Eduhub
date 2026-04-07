from django.db import models
import uuid


from course_app.models import Lesson
from user_app.models import Student
from enumerations.enums import AssignmentStatus

class Assignment(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lesson=models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20, choices=AssignmentStatus.choices, default=AssignmentStatus.PENDING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)