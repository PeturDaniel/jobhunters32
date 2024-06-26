from django.db import models
from employers.models import Employer


class JobOffer(models.Model):
    title = models.CharField(max_length=255)
    percentage = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    due_date = models.DateField()
    start_date = models.DateField()
    description = models.CharField(max_length=9999)
    publish_date = models.DateField()
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, default=1)
   
    def __str__(self):
        return self.title

