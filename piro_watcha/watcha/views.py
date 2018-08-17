from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Comment
from .forms import CommentForm
import urllib.request
import json
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import View
from .forms import UserForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from watcha.models import Movie
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def main(request):
    return render(request, 'watcha/watcha_main.html', )


def check(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'watcha/watcha_check.html', {'movie': movie})


def search(request):
    if request.method == 'GET':
        client_id = "Qecl29vHRGgGNd4hjiov"
        client_secret = "XGZwdGHHfy"

        q = request.GET.get('q')
        encText = urllib.parse.quote("{}".format(q))
        url = "https://openapi.naver.com/v1/search/movie?query=" + encText + "&display=10"  # json 결과
        movie_request = urllib.request.Request(url)
        movie_request.add_header("X-Naver-Client-Id", client_id)
        movie_request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(movie_request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')
            if items:
                high_item = items[0]
                for movie in items:
                    if Movie.objects.filter(title=movie.get('title')):
                        pass
                    else:
                        author = User.objects.get(username='watcha')
                        title = movie.get('title')
                        content = movie.get('subtitle')
                        poster = movie.get('image')
                        Movie.objects.create(author=author, title=title, content=content, poster=poster)
                print(Movie.objects.all())
                return render(request, 'watcha/watcha_search.html', {'high_item': high_item , 'items': items})
            else:
                return render(request, 'watcha/watcha_no_search.html')


def comment_new(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = Comment()
            comment.comment = form.cleaned_data['comment']
            comment.movie = Movie.objects.get(pk=int(form.cleaned_data['movie']))
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



def newaccount(request):
    return render(request, 'watcha/watcha_register.html')


class UserFormView(View):
    form_class = UserForm
    templates_name = 'watcha/watcha_register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.templates_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)  # login
                    return redirect('watcha:main')

        return render(request, self.template_name, {'form': form})


def loginpage(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('watcha:main')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'watcha/watcha_login.html', {'form': form})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'watcha/watcha_main.html', context)

