from django.shortcuts import render
from job_offers.models import JobOffer


def index(request):
    context = {'job_offer': JobOffer.objects.all().order_by('title')}
    return render(request, 'job_offers_page/index.html', context)
