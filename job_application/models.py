from django.db import models
from job_offers.models import JobOffer

# Create your models here.
    """ job recomadadions """
class JobRecomendation(models.Model):
    #TODO


    """job expiriences """
class JobExperience(models.Model):
    place = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

""" job applications """
class Applications(models.Model):
    name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_number = models.IntegerField(null=False)
    city = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    postal_code = models.IntegerField(null=False)
    cover_letter = models.CharField(max_length=9999)
    expirience = models.ForeignKey(JobExperience, on_delete=models.CASCADE)
    recomandation = models.ForeignKey(JobRecomendation, on_delete=models.CASCADE)
    # user = models.ForeignKey() """create table for users/jobhunters"""
    job_offers = models.ForeignKey(JobOffer, on_delete=models.CASCADE)





