from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm # we should import this class
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView

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


#FIXME: User reg forms is not defined
class RegistrationView(FormView):
    template_name = "user_reg.html"
    form_class = UserCreationForm
    redirect_authenticated_url = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistrationView, self).form_valid(form)







