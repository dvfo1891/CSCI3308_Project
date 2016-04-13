from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Course, Assignments
from .forms import SignUpForm

# Create your views here.
def test_main(request):
    user = User.objects.all()
    course = Course.objects.all()
    assigns = Assignments.objects.all()
    return render(request, 'tables/main.html', {'user': user, 'course': course, 'assigns': assigns})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if User.objects.filter(username=request.POST['username']).exists():
            return render(request, 'tables/signups_error.html', {'form' : form})
        else:
            user = form.save(commit=False)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.save()
            login(request,user)
            return redirect('/dashboard')
    else:
        form = SignUpForm()
        return render(request, 'tables/signup.html', {'form' : form})

def dashboard(request):
    return render(request, 'tables/dashboard.html')

