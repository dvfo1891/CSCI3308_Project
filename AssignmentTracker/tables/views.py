from django.shortcuts import render
from .models import User, Course, Assignments

# Create your views here.
def test_main(request):
    user = User.objects.all()
    course = Course.objects.all()
    assigns = Assignments.objects.all()
    return render(request, 'tables/main.html', {'user': user, 'course': course, 'assigns': assigns})


def dashboard(request):
    return render(request, 'tables/dashboard.html')

