from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='logsheet-home'),
    path('reports/', views.reports, name='logsheet-reports'),
]
