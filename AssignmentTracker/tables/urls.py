from django.conf.urls import url
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.views.generic import CreateView
from . import views

urlpatterns = [
    url(r'^$', views.test_main, name='test_main'),
    url(r'^signup/$',(CreateView.as_view(model = User, get_success_url = lambda: reverse('dashboard'), form_class =UserCreationForm, template_name="tables/signups.html")), name='signup'),
    url(r'^search/$', views.search, name='search'),
    url(r'^notif/$', views.notif, name='notif'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^about/$', views.about, name='about'),
    url(r'^help/$', views.helpcenter, name='help'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^search/$', views.search, name='search'),
    # account.
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
]
