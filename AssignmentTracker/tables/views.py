from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Course, Assignments
from .forms import SignUpForm
from django.http import HttpResponse

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

def log_in(request):
    return render(request, 'tables/login.html')

def search(request):
    if request.method == 'GET':
        try:
            keyword = request.GET['keyword']
            if keyword:
                return HttpResponse("searching: %s." % request.GET['keyword'])
            else:
                return HttpResponse("No search keyword provided.")
        except:
            return HttpResponse("search page.")

def notif(request):
    return render(request, 'tables/notif.html')

def dashboard(request):
    return render(request, 'tables/dashboard.html')

def about(request):
    return render(request, 'tables/about.html')

def helpcenter(request):
    return render(request, 'tables/help.html')

def contact(request):
    return render(request, 'tables/contact.html')
