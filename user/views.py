from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.models import JobSeekerProfile
from user.forms.job_seeker_profile_form import JobSeekerProfileForm
from job_application.models import Application
from job_offers.models import JobOffer
from employers.models import Employer

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'job_seeker_page/register.html', {
        'form': UserCreationForm()
    })


def job_seeker_profile(request):
    profile = JobSeekerProfile.objects.filter(user=request.user).first()
    # current_user = request.user
    # job_seeker_profile = JobSeekerProfile.objects.filter(user=current_user).first()
    # job_applications = Application.objects.filter(user_id=job_seeker_profile.id).all()
    # job_offers = []
    # information_temp = {'title': None, 'date': None, 'status': None, 'company': None, 'percentage': None}
    # information = []
    # for job_application in job_applications:
    #     job_offers.append(JobOffer.objects.filter(id=job_application.job_offer_id).first())
    # for job_offer in job_offers:
    #     information_temp['title'] = job_offer.title
    #     company_name = Employer.objects.filter(id=job_offer.employer_id).first().name
    #     information_temp['company'] = company_name
    #     information_temp['percentage'] = job_offer.percentage
    #     information.append(information_temp)
    #     information_temp = {'title': None, 'date': None, 'status': None, 'company': None, 'percentage': None}
    # for application in job_applications:
    #     information_temp['']


    if request.method == 'POST':
        form = JobSeekerProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('job_seeker_profile')
    return render(request, 'job_seeker_page/job_seeker_profile.html', {
        'form': JobSeekerProfileForm(instance=profile),
    })
