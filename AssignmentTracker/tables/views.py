from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Course, Assignments
from .forms import SignUpForm
from django.http import HttpResponse

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

def login(request):
    return HttpResponse('login page')

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
    return HttpResponse("notification page")    

def dashboard(request):
    return render(request, 'tables/dashboard.html')

def about(request):
    return HttpResponse("about page")

def helpcenter(request):
    return HttpResponse("help center page")

def contact(request):
    return HttpResponse("contact page")
