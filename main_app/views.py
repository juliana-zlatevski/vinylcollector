from django.shortcuts import render
from django.http import HttpResponse
from .models import vinyls

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def vinyls_index(request):
    return render(request, 'vinyls/index.html', { 'vinyls': vinyls })