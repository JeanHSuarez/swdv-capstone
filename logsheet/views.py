from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from persons.models import Member
from django.utils import timezone
from django.views.generic import (
         ListView,
         DetailView,
         CreateView,
         UpdateView,
         DeleteView
         )
from .models import LogPost


"""def home(request):

    context = {
        'logposts': LogPost.objects.all()
    }
    return render(request, 'logsheet/home.html', context)"""


class PostListView(ListView):
    model = LogPost
    template_name ='logsheet/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'logposts'
    ordering = ['-signIn']
    paginate_by = 10

class MemberPostListView(ListView):
    model = LogPost
    template_name ='logsheet/member_logposts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'logposts'
    paginate_by = 5

    def get_queryset(self):
        member = get_object_or_404(Member, firstName=self.kwargs.get('firstName'))
        return LogPost.objects.filter(member=member).order_by('-signIn')


class PostDetailView(DetailView):
    model = LogPost

#old code as reference
"""
class PostCreateView(LoginRequiredMixin, CreateView):
    model = LogPost
    fields= ('member', 'signIn', 'signOut')
    success_url = '/logsheet/'

    def form_valid(self, form):
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LogPost
    fields= ('member', 'signIn', 'signOut')
    success_url = '/logsheet/'

    def form_valid(self, form):
        return super().form_valid(form)
#test for current user. Might not need this or need to modify
    def test_func(self):
        logpost = self.get_object()
        if self.request == logpost.member:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LogPost
#test for current user. Might not need this or need to modify
    def test_func(self):
        logpost = self.get_object()
        if self.request == logpost.member:
            return True
        return False
"""

class PostCreateView(CreateView):
    model = LogPost
    fields= ('member', 'signIn', 'signOut')
    success_url = '/logsheet/'

    def form_valid(self, form):
        self.object.signIn = timezone.now()
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = LogPost
    fields= ('member', 'signIn', 'signOut')
    success_url = '/logsheet/'

    def form_valid(self, form):
        self.object.signOut = timezone.now()
        self.object.setDuration()
        return super().form_valid(form)
#test for current user. Might not need this or need to modify

class PostDeleteView(DeleteView):
    model = LogPost
    success_url = '/logsheet/'
#test for current user. Might not need this or need to modify




"""
#This is for the TimeSheet model as it entails user to login before updated

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
"""

def reports(request):
    return render(request, 'logsheet/reports.html', {'title': 'Reports'})
