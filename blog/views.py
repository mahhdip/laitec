from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('published_date')
    #posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def create_post(request):
    me=User.objects.get(username='admin')
    for i in range(100):
        Post.objects.create(author=me,title=f'sample title{i}' , text=f'sample title {i**2}')



    return render(request, 'blog/create_post.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

form = PostForm(request.POST, instance=post)


