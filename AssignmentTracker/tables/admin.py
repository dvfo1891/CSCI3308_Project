from django.contrib import admin
from .models import User, Course, Assignments

# Register your models here.

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Assignments)
