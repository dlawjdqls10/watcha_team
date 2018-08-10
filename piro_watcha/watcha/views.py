from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Comment
from .forms import CommentForm
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


def comment_new(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = Comment()
            comment.comment = form.cleaned_data['comment']
            # comment.movie = form.cleaned_data['movie']
            comment.save()
            return redirect('/watcha/')
    else:
        form = CommentForm()
    return render(request, 'watcha/watcha_comment.html', {
        'form': form,
    })

def main(request):
    return render(request, 'watcha/watcha_main.html')

def profile(request):
    return render(request, 'watcha/watcha_profile.html')

def flavor(request):
    return render(request, 'watcha/watcha_flavor.html')




