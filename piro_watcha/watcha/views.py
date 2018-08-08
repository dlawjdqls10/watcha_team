from django.shortcuts import render, get_object_or_404
from .models import Movie
import urllib.request
import json

# Create your views here.
def main(request):
    return render(request, 'watcha/watcha_main.html',)


def check(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'watcha/watcha_check.html', {'movie': movie})

def search(request):

    if request.method == 'GET':
        client_id = "Qecl29vHRGgGNd4hjiov"
        client_secret = "XGZwdGHHfy"

        q = request.GET.get('q')
        encText = urllib.parse.quote("{}".format(q))
        url = "https://openapi.naver.com/v1/search/movie?query=" + encText + "&display=10"# json 결과
        movie_request = urllib.request.Request(url)
        movie_request.add_header("X-Naver-Client-Id",client_id)
        movie_request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(movie_request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')
            if items:
                return render(request, 'watcha/watcha_search.html', {'items': items})
            else:
                return render(request, 'watcha/watcha_no_search.html')
