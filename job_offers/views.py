from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from job_offers.models import JobOffer


def index(request):
    if 'leit' in request.GET:
        leit = request.GET['leit']
        job_offers = [{
            'title': x.title,
            'description': x.description,
            'due date': x.due_date,
            'percentage': x.percentage
            #meira
        } for x in JobOffer.objects.filter(title__icontains=leit)]
        return JsonResponse({'data': job_offers})
    context = {'job_offers': JobOffer.objects.all().order_by('title')}
    return render(request, 'job_offers_page/index.html', context)


@login_required
def get_job_offer_by_id(request, id):
    return render(request, 'job_offers_page/job_offer_details.html', {
        'job_offer': get_object_or_404(JobOffer, pk=id)
    })
