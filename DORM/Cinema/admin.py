from django.contrib import admin
from .models import (
    Country,
    Actor,
    Genre,
    Producer,
    Company,
    Movie
)

# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    fields = ['name']

class ActorAdmin(admin.ModelAdmin):
    fields = ['name', 'image']

class GenreAdmin(admin.ModelAdmin):
    fields = ['name']

class ProducerAdmin(admin.ModelAdmin):
    fields = ['name', 'image']

class CompanyAdmin(admin.ModelAdmin):
    fields = ['name', 'logo']

class MovieAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'duration', 'country', 'genres', 'release', 'producers', 'cast', 'poster', 'production']

admin.site.register(Actor, ActorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Movie, MovieAdmin)
