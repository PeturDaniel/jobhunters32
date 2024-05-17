from django.shortcuts import render, redirect
from formtools.wizard.views import SessionWizardView
from job_application.forms import JobRecommendationFormSet, JobExperienceFormSet, ApplicationForm, ReviewForm
from job_offers.models import JobOffer
from user.models import JobSeekerProfile
from job_application.models import Application
from django.http import HttpResponseRedirect


def success(request):
    return render(request, 'job_application/success.html')


class JobApplicationWizard(SessionWizardView):
    form_list = [ApplicationForm, JobRecommendationFormSet, JobExperienceFormSet, ReviewForm]
    template_name = 'job_application/job_application_wizard.html'

    def get_context_data(self, form, **kwargs):
        previous_data = {}
        current_step = self.steps.current
        if current_step == '3':
            for count in range(3):
                previous_data[str(count)] = self.get_cleaned_data_for_step(str(count))
            while {} in previous_data['1']:
                previous_data['1'].remove({})
            while {} in previous_data['2']:
                previous_data['2'].remove({})
        context = super(JobApplicationWizard, self).get_context_data(form=form, **kwargs)
        context.update({'previous_cleaned_data': previous_data})
        return context

    def done(self, form_list, **kwargs):
        job_offer_id = self.kwargs.get('job_offer_id')
        job_offer = JobOffer.objects.get(pk=job_offer_id)
        current_user = self.request.user
        job_seeker = JobSeekerProfile.objects.get(user_id=current_user.id)
        if Application.objects.filter(job_offer_id=job_offer_id, user_id=job_seeker.id).exists():
            return redirect('success')

        application_form = form_list[0]
        application = application_form.save(commit=False)
        application.user = job_seeker
        application.job_offer = job_offer
        application.save()
        job_recommendations = self.get_cleaned_data_for_step('1')
        counter = 0
        for job_recommendation in job_recommendations:
            if job_recommendation:
                job_recommendation_form = form_list[1][counter]
                recommendation = job_recommendation_form.save(commit=False)
                recommendation.job_application = application
                recommendation.save()
                counter += 1
        counter = 0
        job_experiences = self.get_cleaned_data_for_step('2')
        for job_experience in job_experiences:
            if job_experience:
                job_experience_form = form_list[2][counter]
                experience = job_experience_form.save(commit=False)
                experience.job_application = application
                experience.save()
                counter += 1
        return HttpResponseRedirect('success')
