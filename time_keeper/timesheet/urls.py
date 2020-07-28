from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='timesheet-home'),
    path('about/', views.about, name='timesheet-about'),
]
