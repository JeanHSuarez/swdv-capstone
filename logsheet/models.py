from django.db import models
from datetime import date
from django.utils import timezone
from persons.models import Employee, Member
from django.urls import reverse
from datetime import date


class LogPost(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    signIn = models.DateTimeField(default=timezone.now)
    signOut = models.DateTimeField(null=True, blank=True)
    duration =  models.FloatField(null=True, blank=True)

    def __repr__(self):
        return "(%r)" % (self.signIn)


    def setDuration(self):
        if not self.signOut:
            return
        delta = self.signOut - self.signIn
        deltaInSeconds = delta.total_seconds()
        deltaInMinutes = deltaInSeconds / 60
        self.duration = deltaInMinutes





class DailyAggregator(models.Model):
    date = models.DateField(default=date.today)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    signInCount = models.IntegerField(default=0, null=False)
    signOutCount = models.IntegerField(default=0, null=False)
    totalDuration = models.FloatField(default=0.0, null=False)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)



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