from django.db import models
from django.utils import timezone
from persons.models import Employee, Member
from django.urls import reverse


class LogPost(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    signIn = models.DateTimeField(default=timezone.now)
    signOut = models.DateTimeField(null=True, blank=True)

    def __repr__(self):
        return "(%r)" % (self.signIn)

#    def get_ablsolute_url(self):
#        return reverse('success')
"""
class TimeSheet(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    signIn = models.DateTimeField(default=timezone.now)
    signOut = models.DateTimeField(null=True, blank=True)

    def __repr__(self):
        return "(%r)" % (self.signIn)

    def get_ablsolute_url(self):
        #timesheet-detail doesn't exist yet
        return reverse('timesheet-detail', kwargs={'pk': self.pk})
"""