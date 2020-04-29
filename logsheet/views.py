from django.shortcuts import render
from django.http import HttpResponse
from .models import LogPost


def home(request):

    context = {
        'logposts': LogPost.objects.all()
    }
    return render(request, 'logsheet/home.html', context)


def reports(request):
    return render(request, 'logsheet/reports.html', {'title': 'Reports'})
