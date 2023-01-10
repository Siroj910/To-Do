from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .models import Task

class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "task_list.html"

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'

class TaskEditView(UpdateView):
    template_name = 'task_edit.html'
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    template_name = "task_delete_confirmation.html"
    model = Task
    success_url = reverse_lazy('task-list')

class TaskCreateView(CreateView):
    template_name = "task_create.html"
    fields = '__all__'
    model = Task
    success_url = reverse_lazy('task-list')





#TODO: Login and registration
class LogInView(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy('task-list')
























# AUTH
#from django.contrib.auth.views import LoginView
# field, redirect_authenticated_user=defautl(False)
# def get_succes_url(self):
#     return reverse_lazy("name")









