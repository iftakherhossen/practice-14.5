from django.shortcuts import render
from .forms import OrdinaryCodersForm, GeeksForGeeksForm

# Create your views here.
def ordinary_coders(request):
    form = OrdinaryCodersForm()
    return render(request, 'ordinary_coders.html', {'form':form})

def geeks_for_geeks(request):
    form = GeeksForGeeksForm()
    return render(request, 'geeks_for_geeks.html', {'form':form})