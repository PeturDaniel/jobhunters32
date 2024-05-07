from django.db import models
from django.utils import timezone


class JobOffer(models.Model):
    title = models.CharField(max_length=255)
    percentage = models.CharField(max_length=255)
    #location = models.ForeignKey()
    category = models.CharField(max_length=255)
    due_date = models.DateField()
    start_date = models.DateField(default=timezone.now())
    description = models.CharField(max_length=255)
    #employer_name = models.ForeignKey()
    #employer_address = models.ForeignKey()
    #employer_link = models.ForeignKey()