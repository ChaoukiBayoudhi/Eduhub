from django.db import models
class CourseStatus(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    PUBLISHED = 'published'
    UNPUBLISHED = 'unpublished'
    ARCHIVED = 'archived'
    PROGRESS = 'progress'
    DELETED = 'deleted'

class InstructorGradeLevel(models.TextChoices):
    ASSISTANT = 'Assistant'
    LECTURER = 'Lecturer'
    PROFESSOR = 'Professor'
    SENIOR_LECTURER = 'Senior Lecturer'
    HEAD_OF_DEPARTMENT = 'Head of Department'
    DEAN = 'Dean'
    PROVOST = 'Provost'
    CHANCELLOR = 'Chancellor'
    OTHER = 'Other'

class StudentLevel(models.IntegerChoices):
    PRIMARY = 1, 'student level 1'
    SECONDARY = 2, 'student level 2'
    HIGH_SCHOOL = 3, 'student level 3'
    COLLEGE = 4, 'student level 4'
    UNIVERSITY = 5, 'student level 5'
    OTHER = 6, 'student level 6'

class EnrollmentStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    ACTIVE = 'active', 'Active'
    COMPLETED = 'completed', 'Completed'
    CANCELLED = 'cancelled', 'Cancelled'
    ON_HOLD = 'on_hold', 'On Hold'

class AssignmentStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    SUBMITTED = 'submitted', 'Submitted'
    GRADED = 'graded', 'Graded'
    FAILED = 'failed', 'Failed'
    PASSED = 'passed', 'Passed'
    ON_HOLD = 'on_hold', 'On Hold'