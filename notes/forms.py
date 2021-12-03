from .models import Note
from django import forms
from django.forms import ModelForm, fields, widgets


class NoteForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Enter Title'}))
    text = forms.CharField(max_length=500, widget=forms.TextInput(attrs={
        'placeholder': 'Write your notes here!'}))

    class Meta:
        model = Note
        fields = ['name', 'text']
