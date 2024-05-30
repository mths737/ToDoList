from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

@login_required
def tasks_list(request):
    if (request.method == 'GET'):
        tasks = Tasks.objects.filter(completed=False)
        if request.path == "/accounts/profile/":
            request.path = ""
            print(request.path)
            return redirect('tasks_list')
        else:
            return render(request, 'tasks_list.html', { 'tasks':tasks })
    else:
        tasks = Tasks.objects.filter(completed=False)
        selecionado = request.POST.get("selecionado")
        task = Tasks.objects.get(id=selecionado)
        if request.POST.get("botao") == "concluido":
            task.completed = True
            task.save()
            msg = 'Tarefa concluída!'
            return render(request, 'tasks_list.html', {'tasks':tasks, 'msg':msg})
        elif request.POST.get("botao") == "excluir":
            Tasks.delete(task)
            msg = 'Tarefa excluida!'
            return render(request, 'tasks_list.html', {'tasks':tasks, 'msg':msg})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
    else:
        return redirect(tasks_list)
    
@login_required
def tasks_completed(request):
    if request.method == 'GET':
        tasks = Tasks.objects.filter(completed=True)
        return render(request, 'tasks_completed.html', {'tasks':tasks})
    else:
        tasks = Tasks.objects.filter(completed=True)
        selecionado = request.POST.get("selecionado")
        task = Tasks.objects.get(id=selecionado)
        if request.POST.get("botao") == "excluir":
            Tasks.delete(task)
            msg = 'Tarefa excluida!'
            return render(request, 'tasks_completed.html', {'tasks':tasks, 'msg':msg})