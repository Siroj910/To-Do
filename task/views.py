from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm # we should import this class
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView

from .models import Task

class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)

        # context['count'] = context['tasks'].filter(complete=False).count()
        return context

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

    def form_invalid(self, form):
        form.instance.user =  self.request.user
        return super(TaskCreateView, self).form_valid(form)

class LogInView(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy('task-list')

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







