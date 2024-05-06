from django.db import models
from django.utils import timezone


# Create your models here.
class JobOffer(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    due_date = models.DateField()
    created_on = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.id})"
