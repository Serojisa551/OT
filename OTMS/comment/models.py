from django.db import models
from register.models import User
from task.models import Task

class Comments(models.Model):
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    related_task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author.username} on Task {self.related_task.task_name}"
