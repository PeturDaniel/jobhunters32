from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from job_offers.models import JobOffer
from django.db.models.functions import Lower
from user.models import JobSeekerProfile
from job_application.models import Application
from employers.models import Employer

def index(request):
    job_offers = JobOffer.objects.all().order_by(Lower('title'))
    employers = Employer.objects.values_list('name', flat=True).order_by(Lower('name'))
    categories = JobOffer.objects.values_list('category', flat=True).order_by(Lower('category'))
    due_date = JobOffer.objects.values_list('due_date', flat=True).order_by('due_date')

    unique_employers = []
    for employer in employers:
        if employer not in unique_employers:
            unique_employers.append(employer)

    unique_categories = []
    for category in categories:
        if category not in unique_categories:
            unique_categories.append(category)



    context = {
        'job_offers': job_offers,
        'unique_employers': unique_employers,
        'unique_categories': unique_categories,
        'due_dates': due_date,
    }

    if request.user.is_authenticated:
        profile = JobSeekerProfile.objects.filter(user=request.user).first()
        print(profile)
        if profile is None:
            job_applications = []
            context['job_applications'] = job_applications
        else:
            job_applications = Application.objects.filter(user_id=profile.id).values_list('job_offer_id', flat=True)
            print(list(job_applications))
            context['job_applications'] = list(job_applications)

    return render(request, 'job_offers_page/index.html', context)


def get_job_offer_by_id(request, id):
    if request.user.is_authenticated:
        profile = JobSeekerProfile.objects.filter(user=request.user).first()
        if profile is not None:
            applications = Application.objects.filter(user_id=profile.id)
            enable = True
            context = {'date': None, 'status': None, 'is_job_seeker': True}
            for application in applications:
                if application.job_offer_id == id:
                    enable = False
                    context['date'] = application.sent_date
                    context['status'] = application.status
            return render(request, 'job_offers_page/job_offer_details.html', {
                'job_offer': get_object_or_404(JobOffer, pk=id),
                'enable': enable,
                'context': context
            })
        else:
            context = {'is_job_seeker': False}
            return render(request, 'job_offers_page/job_offer_details.html', {
                'job_offer': get_object_or_404(JobOffer, pk=id),
                'enable': False,
                'context': context
            })
    else:
        return render(request, 'job_offers_page/job_offer_details.html', {
            'job_offer': get_object_or_404(JobOffer, pk=id),
            'enable': True
        })


