from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Movie, Review, Comment
from .forms import MovieForm, ReviewForm, CommentForm

# Create your views here.
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies,
    }
    return render(request, 'community/index.html', context)

@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('community:movie_detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form
    }
    return render(request, 'community/forms.html', context)

def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = ReviewForm()
    context = {
        'movie': movie,
        'form': form
    }
    return render(request, 'community/movie_detail.html', context)


def review_create(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.movie_title = movie
                review.save()
                return redirect('community:movie_detail', movie.pk)
        else:
            form = ReviewForm()
        context = {
            'form': form,
            'movie': movie,
        }
        return render(request, 'community/forms.html', context)
    else:
        messages.warning(request, "로그인 필수")
        return redirect('accounts:login')

def review_detail(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm()
    context = {
        'movie': movie,
        'review': review,
        'form': form
    }
    return render(request, 'community/review_detail.html', context)

@require_POST
@login_required
def review_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('community:index')

def review_update(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES, instance=review)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = review.user
                review.save()
                return redirect('community:review_detail', movie_pk, review.pk)
        else:
            form = ReviewForm(instance=review)
        context = {
            'form':form
        }
        return render(request, 'community/forms.html', context)
    else:
        messages.warning(request, '본인 글이 아님')
        return redirect('community:index')

@require_POST
@login_required
def comments_create(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.review = review
        comment.save()
    return redirect('community:review_detail', movie_pk, review.pk)

@require_POST
@login_required
def comments_delete(request, movie_pk, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('community:review_detail', movie_pk, review_pk)


def review_like(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_user.filter(id=request.user.pk).exists():
        review.like_user.remove(request.user)
    else:
        review.like_user.add(request.user)
    return redirect('community:review_detail', movie_pk, review.pk)