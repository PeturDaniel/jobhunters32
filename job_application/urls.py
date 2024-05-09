from django.urls import path
from job_application.forms import JobExperienceForm, JobReccomendationForm, ApplicationForm
from job_application.views import JobApplicationWizard


urlpatterns = [
    #http://localhost:8000/umsoknir
    path('job_application_wizard', JobApplicationWizard.as_view([ApplicationForm, JobReccomendationForm, JobExperienceForm]), name='job_application_wizard_start')
]

'''path('', views.index, name="applications-index"),'''