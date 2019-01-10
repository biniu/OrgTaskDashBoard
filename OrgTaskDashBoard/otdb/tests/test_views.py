
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from OrgTaskDashBoard.otdb.models import Project
from OrgTaskDashBoard.otdb.serializers import ProjectSerializer

client = Client()


class ProjectTest(TestCase):
    """ Test class for Project API"""

    def setUp(self):
        """create dummy project objects for API test

        :returns:
        :rtype:

        """
        Project.objects.create(project_name='TestProject_1',
                               project_tags=None,
                               file_path='/tmp/test/test.org')

    def test_get_all_projects(self):
        # get API resonse
        response = client.get(reverse('ProjectViewSet'))
        # get data from DB
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(1, 0)
