from django.db import models
from django.utils import timezone
from persons.models import Employee, Member


class LogPost(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    signIn = models.DateTimeField(default=timezone.now)
    signOut = models.DateTimeField(null=True, blank=True)

    def __repr__(self):
        return "(%r)" % (self.signIn)

class TimeSheet(models.Model):
    member = models.ForeignKey(Employee, on_delete=models.CASCADE)
    signIn = models.DateTimeField(default=timezone.now)
    signOut = models.DateTimeField(null=True, blank=True)

    def __repr__(self):
        return "(%r)" % (self.signIn)
