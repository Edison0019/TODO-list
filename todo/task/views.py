from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    task = Task.objects.all()
    form = TaskForm()
    context = {"task": task,'form':form}
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('tasks:home')
    return render(request,'task/list.html',context)
    



def update_task(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        forms = TaskForm(request.POST,instance=task)
        if forms.is_valid:
            forms.save()
            return redirect('tasks:home')
    return render(request,'task/update.html',{'form':form})

def confirm(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('tasks:home')
    return render(request,'task/confirm.html',{'item':item})

