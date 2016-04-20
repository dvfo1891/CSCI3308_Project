from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.test_main, name='test_main'),
    url(r'^signup/$', views.signup, name='signup'),
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
