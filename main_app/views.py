from django.shortcuts import render, redirect
from .models import Vinyl, Review
from .forms import ReviewForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def vinyls_index(request):
    vinyls = Vinyl.objects.all()
    return render(request, 'vinyls/index.html', { 'vinyls': vinyls})

def vinyls_info(request, vinyl_id):
    vinyl = Vinyl.objects.get(id=vinyl_id)
    review_form = ReviewForm()
    return render(request, 'vinyls/info.html', { 
        'vinyl': vinyl,
        'review_form': review_form
        })

def add_review(request, vinyl_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.vinyl_id = vinyl_id
        new_review.save()
    return redirect('info', vinyl_id = vinyl_id)

    