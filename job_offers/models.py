from django.db import models


class JobOffer(models.Model):
    title = models.CharField(max_length=255)
    percentage = models.CharField(max_length=255)
    #location = models.ForeignKey()
    category = models.CharField(max_length=255)
    due_date = models.DateField()
    start_date = models.DateField()
    description = models.CharField(max_length=255)
    publish_date = models.DateField()
    #employer_name = models.ForeignKey()
    #employer_address = models.ForeignKey()
    #employer_link = models.ForeignKey()

