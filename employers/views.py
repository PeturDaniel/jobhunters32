from django.shortcuts import render, get_object_or_404
from employers.models import Employer


def index(request):
    context = {'employers': Employer.objects.all().order_by('name')}
    return render(request, 'employers_page/index.html', context)


def get_employer_by_id(request, id):
    return render(request, 'employers_page/employer_details.html', {
        'employer': get_object_or_404(Employer, pk=id)
    })
