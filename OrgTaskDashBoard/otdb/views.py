from django.shortcuts import render

# Create your views here.
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from OrgTaskDashBoard.otdb.models import Project
from OrgTaskDashBoard.otdb.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('-date_joined')
    serializer_class = ProjectSerializer
