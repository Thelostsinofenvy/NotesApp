from django.urls import path
from notes import views

urlpatterns = [
    path('', views.home, name='home')
]
