from django import forms
from .models import GreatDev

# Create your forms here.
class GreatDevForm(forms.ModelForm):
     class Meta:
        model = GreatDev
        fields = '__all__'