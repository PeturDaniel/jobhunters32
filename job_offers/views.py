from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from job_offers.models import JobOffer


def index(request):
    context = {'job_offers': JobOffer.objects.all().order_by('title')}
    return render(request, 'job_offers_page/index.html', context)


@login_required
def get_job_offer_by_id(request, id):
    return render(request, 'job_offers_page/job_offer_details.html', {
        'job_offer': get_object_or_404(JobOffer, pk=id)
    })
