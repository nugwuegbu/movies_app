from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from main.models import Movies
# Create your views here.

@login_required
def show(request):
    all_movies = Movies.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(all_movies, 10)
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    return render(request,"movies.html",{"movies":movies})