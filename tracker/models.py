from django.db import models
from datetime import date

class Event(models.Model):
    name = models.CharField(max_length=100)
    last_occurred = models.DateField()

    @property
    def days_since(self):
        return (date.today() - self.last_occurred).days

    def __str__(self):
        return self.name
