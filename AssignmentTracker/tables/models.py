from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Course(models.Model):
    username = models.CharField(max_length=18)
    course = models.CharField(max_length=40)
    difficulty = models.IntegerField(default=1)
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.course


class Assignments(models.Model):
    course = models.CharField(max_length=40)
    assignment = models.CharField(max_length=200)
    start = models.CharField(max_length=10)
    end = models.CharField(max_length=10)
    difficulty = models.IntegerField(default=1)

    def __str__(self):
        return self.assignment

class Notification(models.Model):
    user_from = models.ForeignKey('auth.User', related_name='user_from')
    user_to = models.ForeignKey('auth.User', related_name='user_to')
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=1024)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
