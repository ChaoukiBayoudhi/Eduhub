from django.db import models
from django.db.models.fields import uuid
from django.core.validators import MinValueValidator, MaxValueValidator

from enumerations.enums import CourseStatus
from user_app.models import Instructor
class Course(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)
    description=models.TextField()
    status=models.CharField(max_length=20, choices=CourseStatus.choices, default=CourseStatus.DRAFT)
    price=models.DecimalField(max_digits=10, decimal_places=2, default=0.00,
    validators=[MinValueValidator(0.00,message="Price must be greater than 0"), MaxValueValidator(2000.00,message="Price must be less than 2000")])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    #relationship between Course and Instructor (N-1)
    instructor=models.ForeignKey(Instructor, on_delete=models.SET_NULL,null=True, blank=True)
    class Meta:
        db_table = 'courses'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['title', 'slug']),
        ]
    #__str__ is the method used to return the string representation of the object
    #it's used to display the object in the admin interface
    #it's also used to display the object in the console
    #it's also used to display the object in the API
    def __str__(self)->str:
        return f"{self.title} - {self.instructor.username}"

class Lesson(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=255)
    description=models.TextField()
    video_url=models.URLField()
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    duration=models.DurationField()
    order=models.PositiveIntegerField()
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'lessons'
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        ordering = ['order']
        indexes = [
            models.Index(fields=['course', 'order']),
        ]
    def __str__(self)->str:
        return f"{self.title} - {self.course.title}"