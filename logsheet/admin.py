from django.contrib import admin
from .models import LogPost, DailyAggregator, DailyReport




admin.site.register(LogPost)
admin.site.register(DailyAggregator)
admin.site.register(DailyReport)
