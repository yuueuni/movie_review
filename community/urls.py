from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),

    path('movie_create/', views.movie_create, name='movie_create'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),

    path('<int:movie_pk>/review_create/', views.review_create, name='review_create'),
    path('<int:movie_pk>/review/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('<int:movie_pk>/review/<int:review_pk>/delete/', views.review_delete, name='review_delete'),
    path('<int:movie_pk>/review/<int:review_pk>/update/', views.review_update, name='review_update'),

    path('<int:movie_pk>/review/<int:review_pk>/comments_create/', views.comments_create, name='comments_create'),
    path('<int:movie_pk>/review/<int:review_pk>/comments_delete/<int:comment_pk>/', views.comments_delete, name='comments_delete'),

    path('<int:movie_pk>/review/<int:review_pk>/like/', views.review_like, name='review_like'),
]
