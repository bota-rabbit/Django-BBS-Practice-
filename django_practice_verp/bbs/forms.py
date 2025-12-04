from django import forms
from .models import Post

class SearchForm(forms.Form):
    keyword = forms.CharField(label='検索', max_length=100)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('content', 'user_name')
