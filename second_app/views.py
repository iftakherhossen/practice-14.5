from django.shortcuts import render
from .forms import GreatDevForm

# Create your views here.
def great_dev_medium(request):
    form = GreatDevForm()
    return render(request, 'great_dev_medium.html', {'form':form})