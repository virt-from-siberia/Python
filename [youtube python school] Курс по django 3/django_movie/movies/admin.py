from django.contrib import admin
from .models import Category, Actor, Genre, Movie, MovieShots, Rating, Reviews, RatingStar


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_display_links = ("title",)
    list_filter = ("category", "year",)
    search_fields = ("title", "category__name")


admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
