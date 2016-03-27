from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.test_main, name='test_main'),
    url(r'^dashboard', views.dashboard, name='dashboard')
]
