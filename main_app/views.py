from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Home')

def about(request):
    return HttpResponse('About')

def vinyls(request):
    return HttpResponse('All Vinyls')