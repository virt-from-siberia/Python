from django.contrib import admin
from .models import Category, Actor, Genre, Movie, MovieShots, Rating, Reviews

# Register your models here.


admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(Reviews)
