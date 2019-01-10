from django.db import models
# from djongo import models

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_id = models.IntegerField(primary_key=True)
    project_tags = models.ForeignKey('Tag',
                                     on_delete=models.SET_DEFAULT,
                                     default=None,
                                     null=True)
    file_path = models.CharField(max_length=255)


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)
    tag_id = models.IntegerField(primary_key=True)


class Status(models.Model):
    status_name = models.CharField(max_length=255)
    status_id = models.IntegerField(primary_key=True)


class Task(models.Model):
    task_name = models.CharField(max_length=255)
    task_id = models.IntegerField(primary_key=True)
    task_org_id = models.CharField(max_length=255)  # for org files
    task_level = models.IntegerField()
    task_status = models.ForeignKey('Status',
                                    on_delete=models.SET_DEFAULT,
                                    default=None,
                                     null=True)
    # task_priority =
    task_tags = models.ForeignKey('Tag',
                                  on_delete=models.SET_DEFAULT,
                                  default=None,
                                  null=True)
    task_deadline = models.DateField()
    task_created = models.DateField()
    # task_parent = ???
    task_project_id = models.ForeignKey('Project',
                                        on_delete=models.SET_DEFAULT,
                                        default=None,
                                        null=True)
