from django.shortcuts import render, get_object_or_404
from employers.models import Employer
from job_offers.models import JobOffer
from django.db.models.functions import Lower
from django.utils import timezone


def index(request):
    context = {'employers': Employer.objects.all().order_by(Lower('name'))}
    return render(request, 'employers_page/index.html', context)


def get_employer_by_id(request, id):
    all_job_offers = JobOffer.objects.filter(employer_id=id)
    non_due_job_offers = []
    for job_offer in all_job_offers:
        due_date = job_offer.due_date
        if due_date >= timezone.now().date():
            non_due_job_offers.append(job_offer)
    return render(request, 'employers_page/employer_details.html', {
        'employer': get_object_or_404(Employer, pk=id),
        'job_offers': non_due_job_offers
    })
