from django.urls import path
from job_application.views import JobApplicationWizard, success


urlpatterns = [
    #http://localhost:8000/umsoknir
    path('job_application_wizard/<int:job_offer_id>', JobApplicationWizard.as_view(), name='job_application_wizard_start'),
    path('job_application_wizard/success', success, name='success')
]

'''path('', views.index, name="applications-index"),'''