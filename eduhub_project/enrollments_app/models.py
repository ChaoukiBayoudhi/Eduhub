import uuid

from django.db import models
from course_app.models import Course
from user_app.models import Student

from enumerations.enums import EnrollmentStatus

class Enrollment(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date=models.DateTimeField(auto_now_add=True)
    completion_date=models.DateTimeField(null=True, blank=True)
    status=models.CharField(max_length=20, choices=EnrollmentStatus.choices, default=EnrollmentStatus.PENDING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'enrollments'
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'
        ordering = ['-created_at']
