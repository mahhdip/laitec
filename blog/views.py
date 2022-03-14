from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone
def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('published_date')
    #posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def create_post(request):
    me=User.objects.get(username='admin')
    for i in range(100):
        Post.objects.create(author=me,title=f'sample title{i}' , text=f'sample title {i**2}')
    return render(request, 'blog/create_post.html', {})
