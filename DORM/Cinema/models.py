from django.db import models
from .utils import unique_slug_generator
from .managers import MovieManager

# Create your models here.

class Country(models.Model):
    name = models.CharField('Country Name', max_length=100)
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self, self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

def actor_directory_path(instance, filename):
    return 'Images/Actors/{0}/{1}'.format(instance.name, filename)

class Actor(models.Model):
    name = models.CharField('Full Name', max_length=100)
    image = models.ImageField(default='Images/Actors/default.png', upload_to=actor_directory_path)
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self, self.name)
        super().save(self, *args, **kwargs)

class Genre(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self, self.name)
        super().save(*args, **kwargs)

def producer_directory_path(instance, filename):
    return 'Images/Producers/{0}/{1}'.format(instance.name, filename)

class Producer(models.Model):
    name = models.CharField('Full Name', max_length=100)
    image = models.ImageField(default='Images/Producers/default.png', upload_to=producer_directory_path)
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self, self.name)
        super().save(*args, **kwargs)

def company_directory_path(instance, filename):
    return 'Images/Companies/{0}/{1}'.format(instance.name, filename)

class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(default='Images/Companies/default.png', upload_to=company_directory_path)
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self, self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['name']

def movie_directory_path(instance, filename):
    return 'Images/Movies/{0}/{1}'.format(instance.name, filename)

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    country = models.ManyToManyField(Country)
    genres = models.ManyToManyField(Genre)
    release = models.DateTimeField()
    producers = models.ManyToManyField(Producer)
    cast = models.ManyToManyField(Actor)
    poster = models.ImageField(default='Images/Movies/default.png', upload_to=movie_directory_path)
    production = models.ManyToManyField(Company)
    slug = models.SlugField(unique=True, max_length=255)

    objects = MovieManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self, self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['release']
