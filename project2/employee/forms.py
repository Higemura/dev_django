from django import forms
from .models import Club, Department

class SearchForm(forms.Form):
  club = forms.ModelChoiceField(
    queryset=Club.objects, label='サークル', required=False #requiredはTrueだと必須
  )

  department = forms.ModelChoiceField(
    queryset=Department.objects, label='部署', required=False
  )