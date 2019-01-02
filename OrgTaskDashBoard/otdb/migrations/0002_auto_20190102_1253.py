# Generated by Django 2.1.4 on 2019-01-02 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_name', models.CharField(max_length=255)),
                ('project_id', models.IntegerField(primary_key=True, serialize=False)),
                ('file_path', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_name', models.CharField(max_length=255)),
                ('status_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_name', models.CharField(max_length=255)),
                ('tag_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RenameField(
            model_name='task',
            old_name='created',
            new_name='task_created',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='deadline',
            new_name='task_deadline',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='level',
            new_name='task_level',
        ),
        migrations.AddField(
            model_name='project',
            name='project_tags',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='otdb.Tag'),
        ),
        migrations.AddField(
            model_name='task',
            name='task_project_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='otdb.Project'),
        ),
        migrations.AddField(
            model_name='task',
            name='task_tags',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='otdb.Tag'),
        ),
    ]
