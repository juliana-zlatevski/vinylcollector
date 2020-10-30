from django.shortcuts import render, redirect
from .models import Vinyl, Review, Mood
from .forms import ReviewForm, VinylForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def vinyls_index(request):
    vinyls = Vinyl.objects.all()
    return render(request, 'vinyls/index.html', { 'vinyls': vinyls})


def add_vinyl(request):
    if request.method == 'POST':
        vinyl_form = VinylForm(request.POST)
        if vinyl_form.is_valid():
            new_vinyl = vinyl_form.save()
            return redirect('info', new_vinyl.id)
    else:
        form = VinylForm()
        context = {'form': form}
        return render(request, 'vinyls/new.html', context)
    

def vinyls_info(request, vinyl_id):
    vinyl = Vinyl.objects.get(id=vinyl_id)

    moods_vinyl_doesnt_have = Mood.objects.exclude(id__in = vinyl.moods.all().values_list('id'))

    review_form = ReviewForm()
    return render(request, 'vinyls/info.html', { 
        'vinyl': vinyl,
        'review_form': review_form,
        'moods': moods_vinyl_doesnt_have
    })

def assoc_mood(request, vinyl_id, mood_id):
    vinyl = Vinyl.objects.get(id=vinyl_id)
    mood = Mood.objects.get(id=mood_id)
    vinyl.moods.add(mood)
    return redirect('info', vinyl_id)


def remove_mood(request, vinyl_id, mood_id):
    vinyl = Vinyl.objects.get(id=vinyl_id)
    mood = Mood.objects.get(id=mood_id)
    vinyl.moods.remove(mood)
    return redirect('info', vinyl_id)


def add_review(request, vinyl_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.vinyl_id = vinyl_id
        new_review.save()
    return redirect('info', vinyl_id = vinyl_id)


def delete_vinyl(request, vinyl_id):
    Vinyl.objects.get(id=vinyl_id).delete()
    return redirect('vinyls_index')


def edit_vinyl(request, vinyl_id):
    vinyl = Vinyl.objects.get(id=vinyl_id)
    
    if request.method == 'POST':
        vinyl_form = VinylForm(request.POST, instance=vinyl)
        if vinyl_form.is_valid():
            updated_vinyl = vinyl_form.save()
            return redirect('info', updated_vinyl.id)

    else: 
        form = VinylForm(instance=vinyl)
        context = {'form': form}
        return render(request, 'vinyls/edit.html', context)       