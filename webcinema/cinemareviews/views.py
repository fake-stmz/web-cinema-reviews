from django.shortcuts import render
from .models import Movie, Genre, Reviewer, Review

# Create your views here.
def index(request):
    movies = Movie.objects.all().prefetch_related('genres').prefetch_related('reviews')

    avg_ratings = dict()
    for movie in movies:
        review_count = 0
        avg_ratings[movie.id] = 0
        for review in movie.reviews.all():
            avg_ratings[movie.id] += review.rating
            review_count += 1
        avg_ratings[movie.id] = round(avg_ratings[movie.id] / review_count, 2) if review_count != 0 else 0

    context = {
        'movies': movies,
        'avg_ratings': avg_ratings
    }

    return render(request, 'index.html', context)