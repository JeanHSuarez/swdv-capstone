from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class LogPost(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    signIn = models.DateTimeField(default=timezone.now)
    signOut = models.DateTimeField(default=timezone.now, null=True)

    def __repr__(self):
        return "(%r)" % (self.signIn)
