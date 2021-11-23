from django.shortcuts import render
from .models import Note
from django.http import request, HttpResponse
from django.views.generic import ListView
from django.utils import timezone

# Create your views here.


class HomeView(ListView):
    model = 'Note'
    template_name = "home.html"

    def get_context_data(self):
        return Note.objects.all()
