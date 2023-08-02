from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=100)

    # Add other fields for the team's details (e.g., description, location, contact info)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    # Add other fields related to the appointment (e.g., service type, additional notes)

    def __str__(self):
        return f"{self.user}'s Appointment with {self.team.name} on {self.date} at {self.start_time}"
