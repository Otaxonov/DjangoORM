from django.db import models

class MovieManager(models.Manager):
    def get_genre_movies(self, genre):
        return self.filter(movie__genre=genre)

    def get_country_movies(self, country):
        return self.filter(movie__country=country)

    def get_actor_movies(self, actor):
        return self.filter(movie__cast=actor)

    def get_producer_movies(self, producer):
        return self.filter(movie__producer=producer)

    def get_company_movies(self, company):
        return self.filter(movie__production=company)
