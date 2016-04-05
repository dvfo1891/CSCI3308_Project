from django.shortcuts import render
from .models import User, Course, Assignments
from .forms import SignUpForm

# Create your views here.
def test_main(request):
    user = User.objects.all()
    course = Course.objects.all()
    assigns = Assignments.objects.all()
    return render(request, 'tables/main.html', {'user': user, 'course': course, 'assigns': assigns})

def signups(request):
    if request.method == 'POST':
		form = SignUpForm(request.POST)
		form.save(commit=True)
		return render(request, 'tables/signups.html', {'form' : form})
    else:
		form = SignUpForm()
		return render(request, 'tables/signups.html', {'form' : form})

def dashboard(request):
    return render(request, 'tables/dashboard.html')

