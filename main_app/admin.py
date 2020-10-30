from django.contrib import admin
from .models import Vinyl, Review, Mood

# Register your models here.
admin.site.register(Vinyl)
admin.site.register(Review)
admin.site.register(Mood)