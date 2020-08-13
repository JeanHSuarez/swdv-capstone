from django.urls import path
from django.urls import reverse
from .views import (PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    MemberPostListView,
    MemberListView,
    MemberDetailView,
    MemberUpdateView,
    MemberDeleteView,
    ReportView,
    GenerateReportView
    )
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='logsheet-home'),
    path('logpost/<int:pk>/', PostDetailView.as_view(), name='logpost-detail'),
    path('logpost/new/', PostCreateView.as_view(), name='logpost-create'),
    path('logpost/<int:pk>/update/', PostUpdateView.as_view(), name='logpost-update'),
    path('logpost/<int:pk>/delete/', PostDeleteView.as_view(), name='logpost-delete'),
    path('member/<str:firstName>', MemberPostListView.as_view(), name='member-record'),
    path('members/', MemberListView.as_view(), name='member-list'),
    path('member/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
    path('member/<int:pk>/update/', MemberUpdateView.as_view(), name='member-update'),
    path('member/<int:pk>/delete/', MemberDeleteView.as_view(), name='member-delete'),
    path('reports/', ReportView.as_view(), name='logsheet-reports'),
    path('generatereport/', GenerateReportView.as_view(), name='generate-report')
]
