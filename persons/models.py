from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ssn = models.CharField(max_length=10)
    birthDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Member(Person):
    diagnosis = models.CharField(max_length=100)
    intakeDate = models.DateTimeField(default=timezone.now)
    psychEval = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    dischargeDate = models.DateTimeField(null=True, blank=True)

class Employee(Person):
    jobtitle = models.CharField(max_length = 20)
    salary = models.CharField(max_length = 10)
    startDate = models.DateTimeField(default=timezone.now)
    educAttainment = models.CharField(max_length = 20, null=True, blank=True)
    otherInfo = models.TextField(null=True, blank=True)
