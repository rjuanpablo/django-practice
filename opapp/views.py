from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = "Django Task Manager"
    return render(request, "index.html", {"title": title})

    #return HttpResponse("Index Page")

def about(request):
    return render(request, "about.html")

    #return HttpResponse("About")

def projects(request):
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {"projects": projects})

    #projects = list(Project.objects.values())
    #return JsonResponse(projects, safe=False)
    #return HttpResponse("Projects")

def tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {"tasks": tasks})

    #task = get_object_or_404(Task, id=id)
    #return render(request, "tasks.html", {"task": task})

    #task = Task.objects.get(id=id)
    #return HttpResponse("Task: %s" % task.title)

def create_task(request):
    if request.method == "GET":
        return render(request, "tasks/create_task.html",{
        'form': CreateNewTask(),
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')
    
def create_project(request):
    if request.method == "GET":
        return render(request, "projects/create_project.html", {
        'form': CreateNewProject(),
        })
    else:
        project = Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, "projects/project_detail.html", {'project': project, 'tasks': tasks})

def hello(request, username):
    return HttpResponse("<h1>Hola, %s</h1>" % username)