# from django.shortcuts import render

# Create your views here.
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from OrgTaskDashBoard.otdb.models import Project, Tag, Status, Task
from OrgTaskDashBoard.otdb.serializers import ProjectSerializer, \
    TagSerializer, StatusSerializer, TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('project_name')
    serializer_class = ProjectSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('tag_name')
    serializer_class = TagSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all().order_by('status_name')
    serializer_class = StatusSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('task_created')
    serializer_class = TaskSerializer
