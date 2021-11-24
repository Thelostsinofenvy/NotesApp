from django.shortcuts import render
from .models import Note
from django.http import request, HttpResponse
from django.views.generic import ListView
from django.utils import timezone

# Create your views here.


def home(request):
    context = {'notes': Note.objects.all}
    return render(request, 'home.html', context)
