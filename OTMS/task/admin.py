from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ["task_name","id","status"]

class TaskAssignmentAdmin(admin.ModelAdmin):
    list_display = ["id", "team", "task"]

admin.site.register(Task, TaskAdmin) 
admin.site.register(TaskAssignment, TaskAssignmentAdmin)