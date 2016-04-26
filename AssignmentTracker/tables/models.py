from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Course(models.Model):
    username = models.ForeignKey('auth.User')
    course = models.CharField(max_length=64)
    difficulty = models.IntegerField(default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    url = models.URLField(max_length=256)

    def __str__(self):
        return self.course

class Assignments(models.Model):
    course = models.ForeignKey(Course)
    assignment = models.CharField(max_length=1024)
    start = models.DateTimeField()
    end = models.DateTimeField()
    difficulty = models.IntegerField(default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)])

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
