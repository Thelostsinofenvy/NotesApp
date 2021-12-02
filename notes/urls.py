from django.urls import path
from notes import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new', views.addNote, name='new'),
    path('details/<int:pk>', views.details, name='details'),
    path('edit/<int:pk>', views.edit, name='edit')
]
