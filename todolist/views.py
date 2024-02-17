from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.
def index(request):
    tasks = Tasks.objects.all()
    form = Taskform()
    
    if request.method =='POST':
        form = Taskform(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')
            
            
    context = {'tasks': tasks, 'form':form}
    return render(request,'todolist/list.html', context)

def updateTask(request,pk):
    task = Tasks.objects.get(id = pk)
    form = Taskform(instance=task)
    context = {'form':form}
    
    if request.method == "POST":
        form = Taskform(request.POST,instance=task)
        if form.is_valid:
            form.save()
        return redirect('/')
        
    
    return render(request, 'todolist/update_list.html', context)

def deleteTask(request,pk):
    item= Tasks.objects.get(id = pk)
    
    if request.method == "POST":
         item.delete()
         return redirect('/')
     
    context = {'item': item}
    return render(request,'todolist/delete.html',context)