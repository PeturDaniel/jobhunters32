from django.shortcuts import render
from joboffers.models import JobOffer

# Create your views here.
def job_offers(request):
    return render(request, "joboffers/index.html", {
        "job_offers": JobOffer.objects.all()
    })
