from django.urls import path
from notes import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new', views.addNote, name='new'),
    path('details/<int:id>', views.details, name='details'),
    path('edit/<int:id>', views.edit, name='edit')
]
