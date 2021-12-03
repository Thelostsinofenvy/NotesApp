from django.shortcuts import redirect, render, get_object_or_404
from .models import Note
from .forms import NoteForm

# Create your views here.


def home(request):
    context = {'notes': Note.objects.all}
    return render(request, 'home.html', context)


def addNote(request):
    form = NoteForm()
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, 'new.html', {'form': form})


def details(request, id):
    notes = Note.objects.filter(id=id)
    return render(request, 'details.html', {'notes': notes})


def edit(request, id):
    obj = get_object_or_404(Note, id=id)
    form = NoteForm(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'edit.html', {'form': form})
