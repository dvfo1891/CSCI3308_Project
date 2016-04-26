from django.conf.urls import url
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.views.generic import CreateView
from . import views

urlpatterns = [
    url(r'^$', views.test_main, name='test_main'),
    url(r'^signup/$',(CreateView.as_view(
        model = User, get_success_url = lambda: reverse('dashboard'), 
        form_class =UserCreationForm, 
        template_name="tables/signup.html")), name='signup'),
    url(r'^notif/$', views.notif, name='notif'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^add_course/$', views.add_course, name='add_course'),
    # about.
    url(r'^about/$', views.about, name='about'),
    url(r'^help/$', views.helpcenter, name='help'),
    url(r'^contact/$', views.contact, name='contact'),
    # add class.
    url(r'^search/$', views.search, name='search'),
    url(r'^enroll/(?P<course_pk>[0-9]+)/$', views.enroll, name='enroll'),
    url(r'^enroll/(?P<course_pk>[0-9]+)/confirm/$', views.enroll_confirm, name='enroll_confirm'),
    # account.
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    # course details.
    url(r'^detail/(?P<course_pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^post/(?P<course_pk>[0-9]+)/$', views.post, name='post'),
    url(r'^post/(?P<assign_pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
