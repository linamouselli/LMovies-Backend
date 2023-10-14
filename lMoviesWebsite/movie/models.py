from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class CompanyType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    
class Company(models.Model):
    name = models.CharField(max_length=255)
    counrty = CountryField()
    type = models.ForeignKey(CompanyType, on_delete=models.PROTECT)
    
class Genre(models.Model):
    name = models.CharField(max_length=100)
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    alias = models.CharField(max_length=1000)
    status = models.CharField(max_length=150)
    release_date = models.DateField()
    runtime = models.IntegerField()
    original_country = CountryField()
    language = models.CharField(max_length=255)
    production_company = models.ForeignKey(Company, on_delete=models.PROTECT)
    trailer = models.URLField(max_length=1000)
    poster_image = models.ImageField()
    box_office = models.DecimalField(max_digits=6, decimal_places=2)
    
class MovieGenre(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
class People(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=100)
    role = models.CharField(max_length=255)
    born_in = CountryField()
    birthdate = models.DateField()
    
class MovieCrew(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    people_id = models.ForeignKey(People, on_delete=models.CASCADE)  
    role = models.CharField(max_length=100)
    actor_name = models.CharField(max_length=255)
    
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    country = CountryField()
    birthdate = models.DateField()
    email = models.EmailField()
    preffered_language = models.CharField(max_length=255)

class MovieRating(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    platform = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=2, decimal_places=2)
    
class UserReview(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=2)
    note = models.CharField(max_length=2000)

class UserActivity(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)

class UserGenreFavorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
class UserMovieFavorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
class UserPeopleFavorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    people_id = models.ForeignKey(People, on_delete=models.CASCADE)