from django.shortcuts import render, redirect
from .forms import TaskForm

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('main_page') 
    else:
        form = TaskForm()
    return render(request, 'task/create_task.html', {'form': form})