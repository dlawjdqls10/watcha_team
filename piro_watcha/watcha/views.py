from django.shortcuts import render, get_object_or_404
from .models import Movie


# Create your views here.
def main(request):
    return render(request, 'watcha/watcha_main.html',)


def check(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'watcha/watcha_check.html', {'movie': movie})
