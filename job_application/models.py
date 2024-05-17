from django.db import models
from job_offers.models import JobOffer
from user.models import JobSeekerProfile
from django.utils import timezone


class Application(models.Model):
    name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_number = models.IntegerField(null=False)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.IntegerField(null=False)
    cover_letter = models.CharField(max_length=9999)
    user = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE, related_name='applications')
    sent_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=255, default="Pending")


class JobRecommendation(models.Model):
    job_application = models.ForeignKey(Application, related_name='recommendations', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField()
    contacted = models.BooleanField(default=True)
    role = models.CharField(max_length=255)


class JobExperience(models.Model):
    job_application = models.ForeignKey(Application, related_name='experiences', on_delete=models.CASCADE)
    place = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
