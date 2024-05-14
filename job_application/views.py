from django.shortcuts import render, redirect
from formtools.wizard.views import SessionWizardView
from job_application.forms import JobRecommendationFormSet, JobExperienceFormSet, ApplicationForm
from job_offers.models import JobOffer
from user.models import JobSeekerProfile



def success(request):
    return render(request, 'job_application/success.html')

class JobApplicationWizard(SessionWizardView):
    form_list = [ApplicationForm, JobRecommendationFormSet, JobExperienceFormSet]
    template_name = 'job_application/job_application_wizard.html'
    # def get_form(self, step=None, data=None, files=None):
    #     if step == 'review':
    #         form = ReviewForm(data=data, files=files)
    #         return form
    #     return super().get_form(step, data, files)

    # def get_context_data(self, form, **kwargs):
    #     context = super().get_context_data(form=form, **kwargs)
    #     if self.steps.current == 'review':
    #         context['applicationform'] = self.get_cleaned_data_for_step('applicationform')
    #         context['jobrecommendation'] = self.get_cleaned_data_for_step('jobrecommendation')
    #         context['jobexperience'] = self.get_cleaned_data_for_step('jobexperience')
    #     return context

    def done(self, form_list, **kwargs):
        job_offer_id = self.kwargs.get('job_offer_id')
        print("THETTA ER ID" + str(job_offer_id))
        print("Form list 0 ")
        print(form_list[0])
        for form in form_list[1]:
            print("Thetta er i form list 1")
            print(form)
        for form in form_list[2]:
            print("Thetta er i form list 2")
            print(form)
        # job_offer = JobOffer.objects.get(pk=job_offer_id)
        # current_user = self.request.user
        # job_seeker = JobSeekerProfile.objects.get(user_id=current_user.id)
        # application_form = form_list[0]
        # application = application_form.save(commit=False)
        # application.user = job_seeker
        # application.job_offer = job_offer
        # application.save()
        # job_recommendations = self.get_cleaned_data_for_step('jobrecommendation')
        # counter = 0
        # for job_recommendation in job_recommendations:
        #     if job_recommendation:
        #         job_recommendation_form = form_list[1][counter]
        #         recommendation = job_recommendation_form.save(commit=False)
        #         recommendation.job_application = application
        #         recommendation.save()
        #         counter += 1
        # counter = 0
        # job_experiences = self.get_cleaned_data_for_step('jobexperience')
        # for job_experience in job_experiences:
        #     if job_experience:
        #         job_experience_form = form_list[2][counter]
        #         experience = job_experience_form.save(commit=False)
        #         experience.job_application = application
        #         experience.save()
        #         counter += 1
        return redirect('success')

