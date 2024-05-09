from django import forms
from django_countries.widgets import CountrySelectWidget
from job_application.models import JobExperience, JobRecommendation, Application
import pycountry

class ApplicationForm(forms.ModelForm):
    country_list = [(country.alpha_2, country.name) for country in pycountry.countries]
    country = forms.ChoiceField(widget=CountrySelectWidget, choices=country_list)
    class Meta:
        model = Application
        fields = ['name', 'street_name', 'house_number', 'city', 'country', 'postal_code', 'cover_letter']


class JobReccomendationForm(forms.ModelForm):
    class Meta:
        model = JobRecommendation
        fields = ['name', 'email', 'phone', 'contacted', 'role']


class JobExperienceForm(forms.ModelForm):
    class Meta:
        model = JobExperience
        fields = ['place', 'role', 'start_date', 'end_date']
        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'}), 'end_date': forms.DateInput(attrs={'type': 'date'})}

