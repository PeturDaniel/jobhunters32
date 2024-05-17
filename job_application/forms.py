from django import forms
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
from job_application.models import JobExperience, JobRecommendation, Application
from django.forms import formset_factory


class ApplicationForm(forms.ModelForm):
    country = CountryField().formfield(widget=CountrySelectWidget())
    class Meta:
        model = Application
        fields = ['name', 'street_name', 'house_number', 'city', 'country', 'postal_code', 'cover_letter']


class ReviewForm(forms.Form):
    pass


class JobReccomendationForm(forms.ModelForm):
    class Meta:
        model = JobRecommendation
        fields = ['name', 'email', 'phone', 'role', 'contacted']


class JobExperienceForm(forms.ModelForm):
    class Meta:
        model = JobExperience
        fields = ['place', 'role', 'start_date', 'end_date']
        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'}), 'end_date': forms.DateInput(attrs={'type': 'date'})}

JobRecommendationFormSet = formset_factory(JobReccomendationForm, extra=3)
JobExperienceFormSet = formset_factory(JobExperienceForm, extra=3)