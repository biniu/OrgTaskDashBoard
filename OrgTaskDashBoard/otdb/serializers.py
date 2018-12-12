# from django.contrib.auth.models import User, Group

from rest_framework import serializers
from OrgTaskDashBoard.otdb.models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'project_id', 'file_path')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')