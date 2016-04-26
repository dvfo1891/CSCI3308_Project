from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Course, Assignments
from .forms import SignUpForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from itertools import chain

# Create your views here.
def test_main(request):
    users = User.objects.all()
    course = Course.objects.all()
    assigns = Assignments.objects.all()
    return render(request, 'tables/main.html', {'users': users, 'course': course, 'assigns': assigns})

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
            return redirect(reverse('dashboard'))
    else:
        form = SignUpForm()
        return render(request, 'tables/signup.html', {'form' : form})


def search(request):
    keyword = request.GET['keyword']
    if keyword:
        courses = Course.objects.filter(course__icontains=keyword)
        courses = chain(courses, Course.objects.all().exclude(course__icontains=keyword).order_by('course'))
    else:
        courses = Course.objects.all().order_by('course')
    return render(request, 'tables/search.html', {'courses': courses})

@login_required
def enroll(request, course_pk):
    return render(request, 'tables/enroll.html', {'course': course_pk})

@login_required
def enroll_confirm(request, course_pk):
    course = Course.objects.get(pk=course_pk)
    request.user.course_set.add(course)
    course.users.add(request.user)
    return redirect(reverse('dashboard'))

@login_required
def notif(request):
    return render(request, 'tables/notif.html')

@login_required
def dashboard(request):
    return render(request, 'tables/dashboard.html')

def about(request):
    return render(request, 'tables/about.html')

def helpcenter(request):
    return render(request, 'tables/help.html')

def contact(request):
    return render(request, 'tables/contact.html')

@login_required
def profile(request):
    return render(request, 'tables/profile.html')

def detail(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    return render(request, 'tables/detail.html', {'course': course})
