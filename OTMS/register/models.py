from django.db import models
from django.contrib.auth.models import User 

class Team(models.Model):
    team_name = models.CharField(max_length=255)
    team_leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lead_teams')
    other_team_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.team_name

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    project_status = models.CharField(max_length=255)
    other_project_features = models.TextField()

    def __str__(self):
        return self.project_name

class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"Team member: {self.user.username} - Team: {self.team.team_name}"

class ProjectTeam(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.project.project_name} - {self.team.team_name}"
