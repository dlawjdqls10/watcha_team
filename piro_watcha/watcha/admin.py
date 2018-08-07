from django.contrib import admin

# Register your models here.
from .models import Movie, Genre, Country, Cast, Director

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name']