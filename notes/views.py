from django.http.response import HttpResponse
from django.shortcuts import render
from notes import models
from django.http import request, HttpResponse
# Create your views here.


def home(request):
    return render(request, 'base.html')
