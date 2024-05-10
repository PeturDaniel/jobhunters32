from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from employers.models import Employer


def index(request):
    if 'leit' in request.GET:
        leit = request.GET['leit']
        employers = [{
            'id': x.id,
            'name': x.name,
            'about': x.about,
            'address': x.address,
            'cover_photo': x.cover_photo,
            'profile_photo': x.profile_photo
            #meira
        } for x in Employer.objects.filter(name__icontains=leit)]
        return JsonResponse({'data': employers})
    context = {'employers': Employer.objects.all().order_by('name')}
    return render(request, 'employers_page/index.html', context)


def get_employer_by_id(request, id):
    return render(request, 'employers_page/employer_details.html', {
        'employer': get_object_or_404(Employer, pk=id)
    })
