from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from job_offers.models import JobOffer
from django.db.models.functions import Lower
from user.models import JobSeekerProfile
from job_application.models import Application


def index(request):
    job_offers = JobOffer.objects.all().order_by('title')
    unique_employers = []
    for job_offer in job_offers:
        if job_offer.employer not in unique_employers:
            unique_employers.append(job_offer.employer)
    context = {
        'job_offers': job_offers,
        'unique_employers': unique_employers,
    }
    return render(request, 'job_offers_page/index.html', context)


def get_job_offer_by_id(request, id):
    if request.user.is_authenticated:
        profile = JobSeekerProfile.objects.filter(user=request.user).first()
        applications = Application.objects.filter(user_id=profile.id)
        enable = True
        context = {'date': None, 'status': None}
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
        return render(request, 'job_offers_page/job_offer_details.html', {
            'job_offer': get_object_or_404(JobOffer, pk=id),
            'enable': True
        })
