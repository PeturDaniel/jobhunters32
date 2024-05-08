from django.db import models

class Employer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    cover_photo = models.CharField(max_length=9999)
    profile_photo = models.CharField(max_length=9999)
    about = models.CharField(max_length=9999)
    address = models.CharField(max_length=255)



