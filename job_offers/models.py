from django.db import models
from employers.models import Employer


class JobOffer(models.Model):
    title = models.CharField(max_length=255)
    percentage = models.CharField(max_length=255)
    #location = models.ForeignKey()
    category = models.CharField(max_length=255)
    due_date = models.DateField()
    start_date = models.DateField()
    description = models.CharField(max_length=255)
    publish_date = models.DateField()
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, default=1)
    #employer_name = models.ForeignKey()
    #employer_address = models.ForeignKey()
    #employer_link = models.ForeignKey()

