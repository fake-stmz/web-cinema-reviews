from django.shortcuts import render
from .models import Movie, Genre, Reviewer, Review

# Create your views here.
def index(request):
    movies = Movie.objects.all().prefetch_related('genres')
    return render(request, 'index.html', {'movies': movies})