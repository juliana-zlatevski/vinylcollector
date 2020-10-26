from django.db import models

# Create your models here.
class Vinyl:
    def __init__(self, title, artist, genre, release_year):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.release_year = release_year

vinyls = [
    Vinyl('Dark Side of the Moon', 'Pink Floyd', 'Progressive Rock', 1973),
    Vinyl('Warpaint', 'Warpaint', 'Psychedelic Indie Rock', 2014),
    Vinyl('In Rainbows', 'Radiohead', 'Art Rock', 2007),
    Vinyl('Alice In Chains: Unplugged', 'Alice In Chains', 'Grunge', 1996),
]