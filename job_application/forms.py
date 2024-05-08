from django import forms


class JobExperienceForm(forms.Form):
    place = forms.CharField(max_length=255)
    role = forms.CharField(max_length=255)
    start_date = forms.DateField()
    end_date = forms.DateField()

class JobReccomendationForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    phone = forms.IntegerField()
    contacted = forms.BooleanField()
    role = forms.CharField(max_length=255)

class ApplicationForm(forms.Form):
    name = forms.CharField(max_length=255)
    street_name = forms.CharField(max_length=255)
    house_number = forms.IntegerField(null=False)
    city = forms.CharField(max_length=255)
    country = forms.CharField(max_length=255)
    postal_code = forms.IntegerField(null=False)
    cover_letter = forms.CharField(max_length=9999)