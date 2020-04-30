from django.contrib import admin
from .models import Person, Employee, Member


admin.site.register(Employee)
admin.site.register(Member)
