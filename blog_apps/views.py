from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog_apps.models import *
from .forms import Taskform


# Create your views here.

def to_do(request):
    tasks = Task.objects.all()
    form = Taskform()
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/blog_apps/to_do')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = Taskform(instance=task)

    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/blog_apps/to_do')
    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/blog_apps/to_do')

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)
