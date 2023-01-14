from django.urls import path
from .views import TaskListView, TaskDetailView, LogInView, TaskEditView, TaskDeleteView, TaskCreateView, \
    RegistrationView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name="task-detail"),
    path('accounts/login/', LogInView.as_view(), name='login'),
    path('task/edit/<int:pk>/', TaskEditView.as_view(), name='task-edit'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('logout/', LogoutView.as_view(next_page='task-list'), name='logout'),
    path('registration/', RegistrationView.as_view(), name='reg')

]