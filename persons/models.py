from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image


class Person(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    ssn = models.CharField(max_length=10)
    birthDate = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Member(Person):
    firstName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20, null=True, blank=True)
    lastName = models.CharField(max_length=20)
    diagnosis = models.CharField(max_length=100)
    intakeDate = models.DateTimeField(default=timezone.now)
    psychEval = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    dischargeDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.firstName} Member'

class Employee(Person):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    jobtitle = models.CharField(max_length = 20)
    salary = models.CharField(max_length = 10)
    startDate = models.DateTimeField(default=timezone.now)
    educAttainment = models.CharField(max_length = 20, null=True, blank=True)
    otherInfo = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Employee'
