from django.forms import *
from .models import Course, Assignments
from django.contrib.auth.models import User

class SignUpForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
	
class PostForm(ModelForm):
    class Meta:
        model = Assignments
        fields = ('assignment', 'start', 'end', 'difficulty')