from django.contrib import admin

from user_app.models import Instructor, Student

admin.site.register(Instructor)
admin.site.register(Student)

