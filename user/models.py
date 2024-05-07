from django.contrib.auth.models import User
from django.db import models
from job_offers.models import JobOffer


# Create your models here.
class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)
