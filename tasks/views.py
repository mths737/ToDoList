from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Tasks
from .forms import TaskForm

def verificaUser(user):
    pass

@login_required
def tasks_list(request):
    if (request.method == 'GET'):
        user = request.user
        user_id = User.objects.get(username=user).id
        tasks = Tasks.objects.filter(completed=False, created_by=user_id)
        context = { 
            'tasks':tasks,
            'user_id':user_id
        }
        if request.path == "/accounts/profile/":
            request.path = ""
            return redirect('tasks_list')
        else:
            return render(request, 'tasks_list.html', context)
    else:
        user = request.user
        user_id = User.objects.get(username=user).id
        tasks = Tasks.objects.filter(completed=False, created_by=user_id)
        msg = ""
        selecionado = request.POST.get("selecionado")
        task = 0
        context = { 
            'tasks':tasks,
            'user_id':user_id,
            'msg':msg
        }

        try:
            task = Tasks.objects.get(id=selecionado)
        except:
            pass

        if request.POST.get("botao") == "concluido":
            if task.completed == False:
                task.completed = True
                task.save()
                msg = 'Tarefa concluída!'
                context["msg"] = msg
                return render(request, 'tasks_list.html', context)
            else:
                return render(request, 'tasks_list.html', context)
        elif request.POST.get("botao") == "excluir":
            if task:
                Tasks.delete(task)
                msg = 'Tarefa excluida!'
                context["msg"] = msg
                return render(request, 'tasks_list.html', context)
            else:
                return render(request, 'tasks_list.html', context)

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
        else:
            return redirect('tasks_list')
    else:
        return redirect('tasks_list')
    
@login_required
def tasks_completed(request):
    if request.method == 'GET':
        user = request.user
        user_id = User.objects.get(username=user).id
        tasks = Tasks.objects.filter(completed=True, created_by=user_id)
        context = { 
            'tasks':tasks,
            'user_id':user_id
        }
        return render(request, 'tasks_completed.html', context)
    else:
        user = request.user
        user_id = User.objects.get(username=user).id
        tasks = Tasks.objects.filter(completed=True, created_by=user_id)
        selecionado = request.POST.get("selecionado")
        task = 0
        msg = ""
        context = { 
            'tasks':tasks,
            'user_id':user_id,
            'msg':msg
        }

        try:
            task = Tasks.objects.get(id=selecionado)
        except:
            pass

        if request.POST.get("botao") == "excluir":
            if task:
                Tasks.delete(task)
                msg = 'Tarefa excluida!'
                context["msg"] = msg
                return render(request, 'tasks_completed.html', context)
            else:
                return render(request, 'tasks_completed.html', context)