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

    if request.method == 'POST':
        form = JobSeekerProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('job_seeker_profile')
    return render(request, 'job_seeker_page/job_seeker_profile.html', {
        'form': JobSeekerProfileForm(instance=profile)
    })


def user_applications(request):
    profile = JobSeekerProfile.objects.filter(user=request.user).first()
    job_applications = Application.objects.filter(user_id=profile.id).all()
    information_temp = {'title': None, 'date': None, 'status': None, 'company': None, 'percentage': None, 'id': None, 'photo': None}
    information = []
    for application in job_applications:
        job_offer = JobOffer.objects.filter(id=application.job_offer_id).first()
        employer = Employer.objects.filter(id=job_offer.employer_id).first()
        information_temp['title'] = job_offer.title
        information_temp['date'] = application.sent_date
        information_temp['status'] = application.status
        information_temp['company'] = employer.name
        information_temp['percentage'] = job_offer.percentage
        information_temp['id'] = job_offer.id
        information_temp['photo'] = employer.profile_photo
        information.append(information_temp)
        information_temp = {'title': None, 'date': None, 'status': None, 'company': None, 'percentage': None}

    return render(request, 'job_seeker_page/index.html', {
        'information': information
    })