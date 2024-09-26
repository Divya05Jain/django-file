from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm,CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.db.models import Count

# Create your views here.

def home(request):
    return render(request, 'index.html' )


def register(request):
     return render(request, 'register.html')


def createTask(request):
     form = TaskForm()
     if request.method =='POST':
          form = TaskForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('viewTasks')
          
     context ={'form':form}

     return render(request, 'forms.html', context=context)

def viewTasks(request):
     tasks= Task.objects.all()
     context ={'tasks':tasks}
     return render(request, 'view-form.html', context=context)
 

def updateTask(request,pk):
     task= Task.objects.get(id=pk)
     form= TaskForm(instance=task)

     if request.method == "POST":
          form = TaskForm(request.POST, instance= task)
          if form.is_valid():
               form.save()
               return redirect('viewTasks')
     context ={'form': form}
     return render(request, 'updateForm.html', context=context)

def deleteTask(request, pk):
     task = Task.objects.get(id=pk)
     # form = TaskForm(instance=task)
     if request.method == 'POST':
          task.delete()
          return redirect('viewTasks')
     context ={'object': task}
     return render(request, 'delete-task.html', context=context)

def register(request):
     form = CreateUserForm()
     if request.method == 'POST':
          form = CreateUserForm(request.POST)

          if form.is_valid():
               form.save()
               return redirect('viewTasks')
     context ={'form': form}
     return render(request, 'register.html', context=context)

def login(request):
    form = LoginForm()  # Initialize form for GET request
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # Bind data to form
        if form.is_valid():
            username = form.cleaned_data.get('username')  # Use cleaned_data to access form inputs
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)  # Authenticate user
            if user is not None:
                auth.login(request, user)  # Log in user
                return redirect("dashboard")
            else:
                return HttpResponse("Invalid credentials")
    
    context = {'form': form}
    return render(request, 'login.html', context=context)

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html' )


def logout(request):
     auth.logout(request)
     return redirect("")

