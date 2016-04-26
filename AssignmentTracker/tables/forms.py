from django.forms import *
from .models import Course
from django.contrib.auth.models import User

class SignUpForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
	

class AddCourseForm(ModelForm):
	class Meta:
		model = Course
		fields = ['course', 'difficulty']
