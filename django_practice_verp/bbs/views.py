from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import SearchForm, PostForm


# 一覧表示
def index(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        posts = Post.objects.filter(content__contains=keyword)
    else:
        searchForm = SearchForm()
        posts = Post.objects.all()
        
    context = {
        'message': 'Welcome to Practice BBS',
        'posts': posts,
        'searchForm': searchForm,
    }
    return render(request, 'bbs/index.html', context)

# 個別表示
def detail(request, id):
    post = get_object_or_404(Post, pk=id)

    context = {
        'message': 'Show Post ' + str(id),
        'post': post,        
    }
    return render(request, 'bbs/detail.html', context)

# 新規作成
def new(request):
    postForm = PostForm()

    context = {
        'message': 'New Post',
        'postForm': postForm,        
    }
    return render(request, 'bbs/new.html', context)

# 新規投稿
def create(request):
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            post = postForm.save()

    context = {
        'message': 'Create post ' + str(post.id),
        'post': post,
    }
    return render(request, 'bbs/detail.html', context)

# 編集
def edit(request, id):
    post = get_object_or_404(Post, pk=id)
    postForm = PostForm(instance=post)

    context = {
        'message': 'Edit Post',
        'post': post,
        'postForm': postForm,        
    }
    return render(request, 'bbs/edit.html', context)

# 更新
def update(request, id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=id)
        postForm = PostForm(request.POST, instance=post)
        if postForm.is_valid():
            postForm.save()

    context = {
        'message': 'Update post ' + str(id),
        'post': post,
    }
    return render(request, 'bbs/detail.html', context)

# 削除
def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()

    posts = Post.objects.all()
    context = {
        'message': 'Delete Post ' + str(id),
        'posts': posts,        
    }
    return render(request, 'bbs/index.html', context)


# python manage.py runserver
# http://localhost:8000/
# python manage.py makemigrations
# python manage.py migrate
