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

    @classmethod
    def generateReport(cls, memberId, year, month, day):
        dailyData = LogPost.objects.filter(member_id=memberId, signIn__year=year, signIn__month=month, signIn__day=day)
        signInCount = 0
        signOutCount = 0
        totalDuration = 0
    
        for logpost in dailyData:
            if logpost.signIn:
                signInCount += 1

            if logpost.signOut:
                signOutCount += 1

            if logpost.duration:
                totalDuration += logpost.duration

        summaries = DailyAggregator.objects.filter(member_id=memberId, summaryDate__year=year, summaryDate__month=month, summaryDate__day=day)
        if len(summaries) == 1:
            summary = summaries[0]
        else:
            summary = DailyAggregator(summaryDate=f"{year}-{month:02}-{day:02}", member_id=memberId)
        summary.signInCount = signInCount
        summary.signOutCount = signOutCount
        summary.totalDuration = totalDuration
        summary.save()

    @classmethod
    def generateDailyGrandTotal(cls, year, month, day):
        dailyTotalData = LogPost.objects.filter(signIn__year=year, signIn__month=month, signIn__day=day)
        memberIds = []
        for logpost in dailyTotalData:
            memberIds.append(logpost.member_id)

        for memberId in set(memberIds):
            LogPost.generateReport(memberId, year, month, day)

        signInCount = 0
        signOutCount =  0
        totalDuration =  0

        for logpost in dailyTotalData:
            if logpost.signIn:
                signInCount += 1

            if logpost.signOut:
                signOutCount += 1

            if logpost.duration:
                totalDuration += logpost.duration

        summaries = DailyReport.objects.filter(summaryDate__year=year, summaryDate__month=month, summaryDate__day=day)
        if len(summaries) == 1:
            summary = summaries[0]
        else:
            summary = DailyReport(summaryDate=f"{year}-{month:02}-{day:02}")
        summary.signInCount = signInCount
        summary.signOutCount = signOutCount
        summary.totalDuration = totalDuration
        summary.save()




    def setDuration(self):
        if not self.signOut:
            return
        delta = self.signOut - self.signIn
        deltaInSeconds = delta.total_seconds()
        deltaInMinutes = deltaInSeconds / 60
        self.duration = deltaInMinutes



class DailyAggregator(models.Model):
    summaryDate = models.DateField(default=date.today)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    signInCount = models.IntegerField(default=0, null=False)
    signOutCount = models.IntegerField(default=0, null=False)
    totalDuration = models.FloatField(default=0.0, null=False)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)

    def __repr__(self):
        return f'(summaryDate={self.summaryDate}, memberId={self.member_id}, signInCount={self.signInCount}, signOutCount={self.signOutCount}, totalDuration={self.totalDuration})'


class DailyReport(models.Model):
    summaryDate = models.DateField(default=date.today)
    signInCount = models.IntegerField(default=0, null=False)
    signOutCount = models.IntegerField(default=0, null=False)
    totalDuration = models.FloatField(default=0.0, null=False)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)

    def __repr__(self):
        return f'(summaryDate={self.summaryDate}, signInCount={self.signInCount}, signOutCount={self.signOutCount}, totalDuration={self.totalDuration})'

