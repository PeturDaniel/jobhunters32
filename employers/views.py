from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from employers.models import Employer
from job_offers.models import JobOffer
from django.db.models.functions import Lower


def index(request):
    context = {'employers': Employer.objects.all().order_by(Lower('name'))}
    return render(request, 'employers_page/index.html', context)


def get_employer_by_id(request, id):
    return render(request, 'employers_page/employer_details.html', {
        'employer': get_object_or_404(Employer, pk=id),
        'job_offers': JobOffer.objects.filter(employer_id=id)
    })
