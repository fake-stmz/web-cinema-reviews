from django.shortcuts import render
from .models import Movie, Genre, Reviewer, Review

# Create your views here.
def index(request):
    movies = Movie.objects.all().prefetch_related('genres').prefetch_related('reviews')

    avg_ratings = dict()
    for movie in movies:
        avg_ratings[movie.id] = calculate_rating(movie)

    context = {
        'movies': movies,
        'avg_ratings': avg_ratings
    }

    return render(request, 'index.html', context)

def movie_info(request, movie_id):
    movie = Movie.objects.all().prefetch_related('genres').prefetch_related('reviews').get(id=movie_id)
    reviews = movie.reviews.all().select_related('reviewer')
    avg_rating = calculate_rating(movie)

    context = {
        'movie': movie,
        'reviews': reviews,
        'avg_rating': avg_rating
    }

    return render(request, 'movie.html', context)

def calculate_rating(movie):
    review_count = 0
    result = 0
    for review in movie.reviews.all():
        result += review.rating
        review_count += 1
    result = round(result / review_count, 2) if review_count != 0 else 0
    return result