from django.db import models
from register.models import Team

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    other_task_features = models.TextField(blank=True, null=True)

class TaskAssignment(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f"Task Assignment: Team {self.team.team_name} - Task {self.task.task_name}"
