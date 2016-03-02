from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=18)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username

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
