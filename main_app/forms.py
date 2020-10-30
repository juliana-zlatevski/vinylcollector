from django import forms
from .models import Review, Vinyl

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'rating', 'comment']

class VinylForm(forms.ModelForm):
    class Meta:
        model = Vinyl
        fields = ['title', 'artist', 'genre', 'release_year']