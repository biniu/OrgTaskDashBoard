# from django.contrib.auth.models import User, Group

from rest_framework import serializers
from OrgTaskDashBoard.otdb.models import Project, Tag, Status, Task


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('project_name', 'project_id', 'project_tags', 'file_path')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag_name', 'tag_id')


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ('status_name', 'status_id')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('task_name', 'task_id', 'task_org_id', 'task_level',
                  'task_tags', 'task_deadline', 'task_created',
                  'task_project_id')
