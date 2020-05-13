from django import forms
from .models import Movie, Review, Comment

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'rank']

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label = '',
        widget=forms.TextInput(attrs={'placeholder': '댓글을 입력해주세요.'}),
    )
    class Meta:
        model = Comment
        fields = ['content']