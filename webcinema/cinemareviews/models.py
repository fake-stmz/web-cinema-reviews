from django.db import models
from django.utils import timezone


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=70, unique=True)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name="movies")

class Reviewer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()
    published_at = models.DateTimeField(auto_now_add=timezone.now())