from django.shortcuts import render
from .models import Pofol

# Create your views here.
def portfolio(request):
    portfolios = Pofol.objects
    return render(request, 'portfolio.html', {'portfolios':portfolios})