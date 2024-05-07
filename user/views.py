from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.models import JobSeekerProfile
from user.forms.job_seeker_profile_form import JobSeekerProfileForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'job_seeker_page/register.html', {
        'form': UserCreationForm()
    })

def job_seeker_profile(request):
    profile = JobSeekerProfile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = JobSeekerProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('job_seeker_profile')
    return render(request, 'job_seeker_page/job_seeker_profile.html', {
        'form' : JobSeekerProfileForm(instance=profile)
    })