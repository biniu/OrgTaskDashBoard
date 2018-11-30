# from django.db import models
from djongo import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255)
    project_id = models.IntegerField(primary_key=True)
    file_path = models.CharField(max_length=255)
    # tags = ???

class Task(models.Model):
    task = models.CharField(max_length=255)
    task_id = models.IntegerField(primary_key=True)
    task_org_id = models.CharField(max_length=255)  # for org files
    level = models.IntegerField()
    # status = ???
    # priority = ???
    # tags = ???
    deadline = models.DateField()
    created = models.DateField()
    # parent = ???
    # project_id
