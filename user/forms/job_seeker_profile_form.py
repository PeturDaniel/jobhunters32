from django.forms import ModelForm, widgets
from user.models import JobSeekerProfile


class JobSeekerProfileForm(ModelForm):
    class Meta:
        model = JobSeekerProfile
        exclude = ['id', 'user']
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        }
