from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Movie, Actor, Genre
from .forms import ReviewForm, RatingForm


class GenreYear:
    """dsод информации о актере"""

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


class MoviesView(GenreYear, ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(GenreYear, DetailView):
    model = Movie
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        return context


class AddReviewView(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)

        if form.is_valid():
            form = form.save(commit=False)

            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))

            form.movie = movie
            form.save()

        return redirect(movie.get_absolute_url())


class ActorView(GenreYear, DetailView):
    """dsод информации о актере"""
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = 'name'


class FilterMovieView(GenreYear, ListView):
    """Фильтр фильмов"""

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(genres__in=self.request.GET.getlist('genre'))
        )
        return queryset


class JsonFilterMoviesView(ListView):
    """Фильтр фильмов в json"""

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(genres__in=self.request.GET.getlist('genre'))
        ).distinct().values("title", "tagline", "url", "poster")
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"movies": queryset}, safe=False)
