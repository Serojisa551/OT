from django.contrib import admin
from .models import *

class TeamsAdmin(admin.ModelAdmin):
    list_display = ["id", "team_name", "team_leader"]

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ["id", "project_name", "project_status"]

class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "team"]

class ProjectTeamsAdmin(admin.ModelAdmin):
    list_display = ["id", "project", "team"]

admin.site.register(Team, TeamsAdmin)
admin.site.register(Project, ProjectsAdmin)
admin.site.register(TeamMember, TeamMembersAdmin)
admin.site.register(ProjectTeam, ProjectTeamsAdmin)
