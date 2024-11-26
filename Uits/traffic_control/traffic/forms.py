from django import forms
from .models import Owner, Fine, Expiry

class SearchForm(forms.Form):
    licence_number = forms.CharField(max_length=20, label='Enter Licence Number')
    
class SearchByNIDAndDOBForm(forms.Form):
    nid = forms.CharField(max_length=20, label="National ID")
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Date of Birth"
    )