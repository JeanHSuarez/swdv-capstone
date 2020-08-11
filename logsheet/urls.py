from django.urls import path
from django.urls import reverse
from .views import (PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    MemberPostListView,
    ReportView,
    MemberDetailView,
    GenerateReportView
    )
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='logsheet-home'),
    path('member/<str:firstName>', MemberPostListView.as_view(), name='member-record'),
    path('logpost/<int:pk>/', PostDetailView.as_view(), name='logpost-detail'),
    path('logpost/new/', PostCreateView.as_view(), name='logpost-create'),
    path('logpost/<int:pk>/update/', PostUpdateView.as_view(), name='logpost-update'),
    path('logpost/<int:pk>/delete/', PostDeleteView.as_view(), name='logpost-delete'),
    path('reports/', ReportView.as_view(), name='logsheet-reports'),
    path('member/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
    path('generatereport/', GenerateReportView.as_view(), name='generate-report')
]
