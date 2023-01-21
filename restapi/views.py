from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from task.models import Task
from .serializers import TaskSerializers

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    