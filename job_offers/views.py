from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from job_offers.models import JobOffer
from job_application.models import Application
from user.models import JobSeekerProfile


def index(request):
    if 'leit' in request.GET:
        leit = request.GET['leit']
        job_offers = [{
            'id': x.id,
            'title': x.title,
            'description': x.description,
            'due_date': x.due_date,
            'percentage': x.percentage,
            'employer_photo': x.employer.profile_photo
            #meira
        } for x in JobOffer.objects.filter(title__icontains=leit)]
        return JsonResponse({'data': job_offers})
    context = {'job_offers': JobOffer.objects.all().order_by('title')}
    return render(request, 'job_offers_page/index.html', context)


def get_job_offer_by_id(request, id):
    profile = JobSeekerProfile.objects.filter(user=request.user).first()
    enable = True
    applications = Application.objects.filter(user_id=profile.id)
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
