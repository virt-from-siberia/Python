from django.shortcuts import render

# Create your views here.
from django.views import View

from .models import Movie


class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movies.html", {"movie_list": movies})
