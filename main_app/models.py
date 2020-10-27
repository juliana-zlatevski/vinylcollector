from django.db import models

# Create your models here.

RATINGS = [
    ('5', '5/5'),
    ('4', '4/5'),
    ('3', '3/5'),
    ('2', '2/5'),
    ('1', '1/5'),
    ('0', '0/5')
]

class Vinyl(models.Model):
    title = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 100)
    release_year = models.IntegerField()

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.CharField(max_length = 50)
    comment = models.TextField(max_length = 500)
    rating = models.CharField(
        max_length = 1,
        choices=RATINGS,
        default=RATINGS[0][0]
    )

    vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_rating_display()} by {self.user} - comments: {self.comment}'
