from django.db import models
from job_offers.models import JobOffer

# Create your models here.

class JobRecommendation(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.IntegerField()
    contacted = models.BooleanField(default=True)
    role = models.CharField(max_length=255)

class JobExperience(models.Model):
    place = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

class Application(models.Model):
    name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_number = models.IntegerField(null=False)
    city = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    postal_code = models.IntegerField(null=False)
    cover_letter = models.CharField(max_length=9999)
    experience = models.ForeignKey(JobExperience, on_delete=models.CASCADE, related_name='applications')
    recommendation = models.ForeignKey(JobRecommendation, on_delete=models.CASCADE, related_name='applications')
    # user = models.ForeignKey() """create table for users/jobhunters"""
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE, related_name='applications')

