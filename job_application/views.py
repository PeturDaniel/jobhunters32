#from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from job_application.forms import JobReccomendationForm, JobExperienceForm, ApplicationForm

# Create your views here.
#def index(request):
 #   return render(request, 'job_application/index.html')

class JobApplicationWizard(SessionWizardView):
    form_list = [ApplicationForm, JobReccomendationForm, JobExperienceForm]
    template_name = 'job_application/job_application_wizard.html'
    def done(self, form_list, **kwargs):
        #do_something_with_the_form_data(form_list)
        job_application = form_list[0]
        job_reccomendation = form_list[1]
        job_experience = form_list[2]
        return HttpResponseRedirect('/lausstorf')